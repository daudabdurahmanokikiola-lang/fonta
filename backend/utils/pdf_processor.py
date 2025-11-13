# ===========================================
# FONTA AI STUDY COMPANION - PDF PROCESSOR
# ===========================================

"""
PDF text extraction and chunking utilities.
Handles large PDFs (up to 400 pages) with overlap for context preservation.
"""

import fitz  # PyMuPDF
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)

class PDFProcessor:
    """PDF text extraction and chunking."""

    def __init__(self, chunk_size: int = 2000, overlap: int = 200):
        """
        Initialize PDF processor.

        Args:
            chunk_size: Target words per chunk (1500-2500 range)
            overlap: Words to overlap between chunks for context
        """
        self.chunk_size = chunk_size
        self.overlap = overlap

    def extract_text_from_pdf(self, pdf_path: str) -> Dict[str, any]:
        """
        Extract text from PDF with page information.

        Args:
            pdf_path: Path to PDF file

        Returns:
            Dict with 'text', 'pages', and 'page_texts' (list of page texts with page numbers)
        """
        try:
            doc = fitz.open(pdf_path)
            full_text = ""
            page_texts = []

            for page_num in range(len(doc)):
                page = doc[page_num]
                page_text = page.get_text()

                if page_text.strip():
                    full_text += page_text + "\n\n"
                    page_texts.append({
                        "page": page_num + 1,
                        "text": page_text.strip()
                    })

            doc.close()

            return {
                "text": full_text.strip(),
                "pages": len(doc),
                "page_texts": page_texts
            }

        except Exception as e:
            logger.error(f"PDF extraction error: {e}")
            raise Exception(f"Failed to extract text from PDF: {str(e)}")

    def chunk_text(self, text: str, page_info: List[Dict] = None) -> List[Dict[str, any]]:
        """
        Chunk text into overlapping segments.

        Args:
            text: Full text to chunk
            page_info: Optional page information for tracking source pages

        Returns:
            List of chunks with text and page hints
        """
        words = text.split()
        chunks = []

        i = 0
        chunk_index = 0

        while i < len(words):
            # Get chunk with specified size
            chunk_words = words[i:i + self.chunk_size]
            chunk_text = " ".join(chunk_words)

            # Determine page range for this chunk if page_info provided
            page_hint = None
            if page_info:
                # Simple heuristic: estimate page based on position in text
                progress = i / len(words)
                estimated_page = int(progress * len(page_info)) + 1
                page_hint = f"p. {estimated_page}"

            chunks.append({
                "chunk_index": chunk_index,
                "text": chunk_text,
                "word_count": len(chunk_words),
                "page_hint": page_hint
            })

            # Move forward by chunk_size minus overlap
            i += self.chunk_size - self.overlap
            chunk_index += 1

            # Break if we're at the end
            if i >= len(words):
                break

        logger.info(f"Created {len(chunks)} chunks from text with {len(words)} words")
        return chunks

    def process_pdf(self, pdf_path: str) -> Dict[str, any]:
        """
        Complete PDF processing: extract and chunk.

        Args:
            pdf_path: Path to PDF file

        Returns:
            Dict with extracted data and chunks
        """
        extraction_result = self.extract_text_from_pdf(pdf_path)
        chunks = self.chunk_text(
            extraction_result["text"],
            extraction_result.get("page_texts")
        )

        return {
            "text": extraction_result["text"],
            "pages": extraction_result["pages"],
            "chunks": chunks,
            "total_words": len(extraction_result["text"].split())
        }
