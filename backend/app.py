from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv
from lib.database import database

# Load environment variables
load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    # Startup
    await database.connect()
    yield
    # Shutdown
    await database.disconnect()

app = FastAPI(
    title="Fonta AI Study Companion API",
    description="AI-powered study companion for Nigerian and African students",
    version="1.0.0",
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

@app.get("/")
def read_root():
    return {
        "message": "Fonta AI Study Companion API",
        "status": "running",
        "version": "1.0.0"
    }

@app.get("/api/test")
def test_endpoint():
    return {
        "status": "success", 
        "data": "FastAPI backend is connected",
        "database": "MongoDB"
    }

@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    try:
        # Test database connection
        await database.client.admin.command('ping')
        return {
            "status": "healthy",
            "database": "connected",
            "api": "running"
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }

