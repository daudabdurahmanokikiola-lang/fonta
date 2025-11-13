# ===========================================
# FONTA AI STUDY COMPANION - QUIZ ROUTES
# ===========================================

"""
API routes for quiz generation with pagination and attempt limits.
Generates 50 questions (35 MCQ + 15 short answer) with 5 questions per page.
"""

from datetime import datetime
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
import logging

from models.gemini_ai import gemini_ai
from utils.db import get_quizzes_collection, get_summaries_collection, get_users_collection

logger = logging.getLogger(__name__)
router = APIRouter()

# Free user limits
FREE_QUIZ_ATTEMPT_LIMIT = 2
QUESTIONS_PER_PAGE = 5

class GenerateQuizRequest(BaseModel):
    user_id: str
    summary_id: str

class GenerateQuizResponse(BaseModel):
    quiz_id: str
    total_questions: int
    total_pages: int
    created_at: str

class QuizPageResponse(BaseModel):
    quiz_id: str
    page: int
    total_pages: int
    questions: List[dict]

@router.post("/api/generate-quiz", response_model=GenerateQuizResponse)
async def generate_quiz(request: GenerateQuizRequest):
    """
    Generate a 50-question quiz from a summary.

    Args:
        user_id: User ID for attempt tracking
        summary_id: Summary ID to generate quiz from

    Returns:
        Quiz ID and pagination info
    """
    try:
        # Check user's quiz attempt limit
        users_collection = get_users_collection()
        user = users_collection.find_one({"_id": request.user_id})

        if not user:
            # Create user record if doesn't exist
            user = {
                "_id": request.user_id,
                "quiz_attempts": 0,
                "subscription_type": "free",
                "created_at": datetime.utcnow().isoformat()
            }
            users_collection.insert_one(user)

        # Check if free user has exceeded attempts
        if user.get("subscription_type") == "free":
            quiz_attempts = user.get("quiz_attempts", 0)
            if quiz_attempts >= FREE_QUIZ_ATTEMPT_LIMIT:
                raise HTTPException(
                    status_code=402,
                    detail="Upgrade to premium to generate more quizzes. Free users are limited to 2 quiz generations."
                )

        # Fetch summary
        from bson import ObjectId
        summaries_collection = get_summaries_collection()
        summary = summaries_collection.find_one({"_id": ObjectId(request.summary_id)})

        if not summary:
            raise HTTPException(status_code=404, detail="Summary not found")

        logger.info(f"Generating quiz for summary: {request.summary_id}")

        # Generate quiz questions
        questions = gemini_ai.generate_quiz(summary['summary'], num_questions=50)

        if len(questions) < 50:
            logger.warning(f"Generated only {len(questions)} questions, expected 50")

        # Store quiz in database
        quizzes_collection = get_quizzes_collection()
        quiz_doc = {
            "user_id": request.user_id,
            "summary_id": request.summary_id,
            "questions": questions,
            "total_questions": len(questions),
            "created_at": datetime.utcnow().isoformat()
        }

        result = quizzes_collection.insert_one(quiz_doc)
        quiz_id = str(result.inserted_id)

        # Increment user's quiz attempt count
        users_collection.update_one(
            {"_id": request.user_id},
            {"$inc": {"quiz_attempts": 1}}
        )

        total_pages = (len(questions) + QUESTIONS_PER_PAGE - 1) // QUESTIONS_PER_PAGE

        logger.info(f"Quiz generated with ID: {quiz_id}, {len(questions)} questions")

        return GenerateQuizResponse(
            quiz_id=quiz_id,
            total_questions=len(questions),
            total_pages=total_pages,
            created_at=quiz_doc['created_at']
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error generating quiz: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to generate quiz: {str(e)}")

@router.get("/api/quiz/{quiz_id}", response_model=QuizPageResponse)
async def get_quiz_page(
    quiz_id: str,
    page: int = Query(1, ge=1, description="Page number (1-indexed)")
):
    """
    Get a specific page of quiz questions.

    Args:
        quiz_id: Quiz ID
        page: Page number (default 1)

    Returns:
        5 questions for the requested page
    """
    try:
        from bson import ObjectId
        quizzes_collection = get_quizzes_collection()

        quiz = quizzes_collection.find_one({"_id": ObjectId(quiz_id)})

        if not quiz:
            raise HTTPException(status_code=404, detail="Quiz not found")

        questions = quiz.get('questions', [])
        total_questions = len(questions)
        total_pages = (total_questions + QUESTIONS_PER_PAGE - 1) // QUESTIONS_PER_PAGE

        if page > total_pages:
            raise HTTPException(status_code=400, detail=f"Page {page} does not exist. Total pages: {total_pages}")

        # Calculate pagination indices
        start_idx = (page - 1) * QUESTIONS_PER_PAGE
        end_idx = min(start_idx + QUESTIONS_PER_PAGE, total_questions)

        page_questions = questions[start_idx:end_idx]

        return QuizPageResponse(
            quiz_id=quiz_id,
            page=page,
            total_pages=total_pages,
            questions=page_questions
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching quiz page: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/quizzes")
async def get_user_quizzes(user_id: str):
    """Get all quizzes for a user."""
    try:
        quizzes_collection = get_quizzes_collection()

        quizzes = list(quizzes_collection.find({"user_id": user_id}).sort("created_at", -1))

        # Convert ObjectIds to strings and remove full question lists
        for quiz in quizzes:
            quiz['_id'] = str(quiz['_id'])
            quiz['question_count'] = len(quiz.get('questions', []))
            # Remove full questions to reduce payload size
            if 'questions' in quiz:
                del quiz['questions']

        return {
            "status": "success",
            "count": len(quizzes),
            "data": quizzes
        }

    except Exception as e:
        logger.error(f"Error fetching quizzes: {e}")
        raise HTTPException(status_code=500, detail=str(e))
