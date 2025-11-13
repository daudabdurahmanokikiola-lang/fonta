from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
import logging
from dotenv import load_dotenv
from utils.db import db_manager

# Import routers
from routes import summarize, quiz, homework

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    # Startup
    try:
        db_manager.connect()
        logger.info("Database connected successfully")
    except Exception as e:
        logger.error(f"Failed to connect to database: {e}")

    yield

    # Shutdown
    try:
        db_manager.disconnect()
        logger.info("Database disconnected successfully")
    except Exception as e:
        logger.error(f"Error during shutdown: {e}")

app = FastAPI(
    title="Fonta AI Study Companion API",
    description="AI-powered study companion for Nigerian and African students with Gemini AI",
    version="2.0.0",
    lifespan=lifespan
)

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(summarize.router, tags=["Summarization"])
app.include_router(quiz.router, tags=["Quiz Generation"])
app.include_router(homework.router, tags=["Homework Help"])

@app.get("/")
def read_root():
    return {
        "message": "Fonta AI Study Companion API",
        "status": "running",
        "version": "2.0.0",
        "features": [
            "PDF Summarization with context preservation",
            "50-question quiz generation with pagination",
            "Step-by-step homework help"
        ]
    }

@app.get("/api/test")
def test_endpoint():
    return {
        "status": "success",
        "data": "FastAPI backend is connected",
        "database": "MongoDB",
        "ai": "Gemini Pro"
    }

@app.get("/api/health")
def health_check():
    """Health check endpoint."""
    try:
        # Test database connection
        db_manager.client.admin.command('ping')

        # Check if Gemini API key is configured
        gemini_configured = bool(os.getenv("GEMINI_API_KEY"))

        return {
            "status": "healthy",
            "database": "connected",
            "api": "running",
            "gemini_ai": "configured" if gemini_configured else "not_configured"
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }

