# ===========================================
# FONTA AI STUDY COMPANION - HOMEWORK ROUTES
# ===========================================

"""
API routes for homework help with step-by-step solutions.
Provides detailed explanations with tips and study recommendations.
"""

from datetime import datetime
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import logging

from models.gemini_ai import gemini_ai
from utils.db import get_homework_collection

logger = logging.getLogger(__name__)
router = APIRouter()

class HomeworkHelpRequest(BaseModel):
    user_id: str
    question: str
    topic: Optional[str] = None
    difficulty: Optional[str] = None

class HomeworkHelpResponse(BaseModel):
    request_id: str
    question: str
    final_answer: str
    step_by_step: List[str]
    tips: List[str]
    created_at: str

@router.post("/api/homework-helper", response_model=HomeworkHelpResponse)
async def get_homework_help(request: HomeworkHelpRequest):
    """
    Get step-by-step homework help.

    Args:
        user_id: User ID for tracking
        question: Student's question
        topic: Optional subject/topic
        difficulty: Optional difficulty level

    Returns:
        Detailed solution with steps and tips
    """
    try:
        logger.info(f"Processing homework help request for user: {request.user_id}")

        # Generate homework solution
        solution = gemini_ai.get_homework_help(
            question=request.question,
            topic=request.topic,
            difficulty=request.difficulty
        )

        # Store request in database
        homework_collection = get_homework_collection()
        homework_doc = {
            "user_id": request.user_id,
            "question": request.question,
            "topic": request.topic,
            "difficulty": request.difficulty,
            "solution": solution,
            "created_at": datetime.utcnow().isoformat()
        }

        result = homework_collection.insert_one(homework_doc)
        request_id = str(result.inserted_id)

        logger.info(f"Homework help saved with ID: {request_id}")

        return HomeworkHelpResponse(
            request_id=request_id,
            question=request.question,
            final_answer=solution.get('final_answer', ''),
            step_by_step=solution.get('step_by_step', []),
            tips=solution.get('tips', []),
            created_at=homework_doc['created_at']
        )

    except Exception as e:
        logger.error(f"Error processing homework help: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to generate homework help: {str(e)}")

@router.get("/api/homework/{request_id}")
async def get_homework_request(request_id: str):
    """Get a specific homework help request by ID."""
    try:
        from bson import ObjectId
        homework_collection = get_homework_collection()

        homework = homework_collection.find_one({"_id": ObjectId(request_id)})

        if not homework:
            raise HTTPException(status_code=404, detail="Homework request not found")

        # Convert ObjectId to string
        homework['_id'] = str(homework['_id'])
        return homework

    except Exception as e:
        logger.error(f"Error fetching homework request: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/homework")
async def get_user_homework(user_id: str):
    """Get all homework help requests for a user."""
    try:
        homework_collection = get_homework_collection()

        homework_list = list(homework_collection.find({"user_id": user_id}).sort("created_at", -1))

        # Convert ObjectIds to strings
        for homework in homework_list:
            homework['_id'] = str(homework['_id'])

        return {
            "status": "success",
            "count": len(homework_list),
            "data": homework_list
        }

    except Exception as e:
        logger.error(f"Error fetching homework requests: {e}")
        raise HTTPException(status_code=500, detail=str(e))
