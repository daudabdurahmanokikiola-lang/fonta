# ===========================================
# FONTA AI STUDY COMPANION - SUMMARIZE ROUTES
# ===========================================

"""
API routes for PDF summarization with context preservation.
Handles large PDFs with chunking and verbatim definition extraction.
"""

import os
import tempfile
from datetime import datetime
from fastapi import APIRouter, File, UploadFile, Form, HTTPException
from pydantic import BaseModel
from typing import Optional
import logging

from utils.pdf_processor import PDFProcessor
from models.gemini_ai import gemini_ai
from utils.db import get_summaries_collection

logger = logging.getLogger(__name__)
router = APIRouter()

class SummarizeResponse(BaseModel):
    summary_id: str
    file_name: str
    pages: int
    total_words: int
    summary: dict
    created_at: str

@router.post("/api/summarize-pdf", response_model=SummarizeResponse)
async def summarize_pdf(
    file: UploadFile = File(...),
    user_id: str = Form(...)
):
    """
    Summarize a PDF file with context-preserved chunking.

    Args:
        file: PDF file upload
        user_id: User ID for tracking

    Returns:
        Summary with verbatim definitions, bullets, and question-style prompts
    """
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    temp_path = None

    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
            content = await file.read()
            tmp.write(content)
            temp_path = tmp.name

        logger.info(f"Processing PDF: {file.filename} for user: {user_id}")

        # Process PDF: extract and chunk
        pdf_processor = PDFProcessor(chunk_size=2000, overlap=200)
        pdf_data = pdf_processor.process_pdf(temp_path)

        logger.info(f"PDF processed: {pdf_data['pages']} pages, {len(pdf_data['chunks'])} chunks")

        # Summarize each chunk
        chunk_summaries = []
        for chunk in pdf_data['chunks']:
            try:
                chunk_summary = gemini_ai.summarize_chunk(
                    chunk['text'],
                    chunk.get('page_hint')
                )
                chunk_summaries.append(chunk_summary)
                logger.info(f"Summarized chunk {chunk['chunk_index'] + 1}/{len(pdf_data['chunks'])}")
            except Exception as e:
                logger.error(f"Error summarizing chunk {chunk['chunk_index']}: {e}")
                # Continue with other chunks
                continue

        if not chunk_summaries:
            raise HTTPException(status_code=500, detail="Failed to summarize any chunks")

        # Merge chunk summaries
        logger.info("Merging chunk summaries...")
        final_summary = gemini_ai.merge_chunk_summaries(chunk_summaries)

        # Store in database
        summaries_collection = get_summaries_collection()
        summary_doc = {
            "user_id": user_id,
            "file_name": file.filename,
            "pages": pdf_data['pages'],
            "total_words": pdf_data['total_words'],
            "summary": final_summary,
            "created_at": datetime.utcnow().isoformat()
        }

        result = summaries_collection.insert_one(summary_doc)
        summary_id = str(result.inserted_id)

        logger.info(f"Summary saved with ID: {summary_id}")

        return SummarizeResponse(
            summary_id=summary_id,
            file_name=file.filename,
            pages=pdf_data['pages'],
            total_words=pdf_data['total_words'],
            summary=final_summary,
            created_at=summary_doc['created_at']
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing PDF: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to process PDF: {str(e)}")

    finally:
        # Clean up temporary file
        if temp_path and os.path.exists(temp_path):
            os.unlink(temp_path)

@router.get("/api/summaries/{summary_id}")
async def get_summary(summary_id: str):
    """Get a specific summary by ID."""
    try:
        from bson import ObjectId
        summaries_collection = get_summaries_collection()

        summary = summaries_collection.find_one({"_id": ObjectId(summary_id)})

        if not summary:
            raise HTTPException(status_code=404, detail="Summary not found")

        # Convert ObjectId to string
        summary['_id'] = str(summary['_id'])
        return summary

    except Exception as e:
        logger.error(f"Error fetching summary: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/summaries")
async def get_user_summaries(user_id: str):
    """Get all summaries for a user."""
    try:
        summaries_collection = get_summaries_collection()

        summaries = list(summaries_collection.find({"user_id": user_id}).sort("created_at", -1))

        # Convert ObjectIds to strings
        for summary in summaries:
            summary['_id'] = str(summary['_id'])

        return {
            "status": "success",
            "count": len(summaries),
            "data": summaries
        }

    except Exception as e:
        logger.error(f"Error fetching summaries: {e}")
        raise HTTPException(status_code=500, detail=str(e))
