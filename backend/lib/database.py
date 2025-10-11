# ===========================================
# FONTA AI STUDY COMPANION - DATABASE CONNECTION
# ===========================================

"""
MongoDB database connection and configuration for Fonta AI Study Companion.

This module handles:
- MongoDB connection setup
- Database configuration
- Connection management
- Error handling

Author: Fonta AI Team
Version: 1.0.0
"""

import os
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class Database:
    """MongoDB database connection manager."""
    
    def __init__(self):
        self.client: Optional[AsyncIOMotorClient] = None
        self.database = None
        self.mongo_url = os.getenv("MONGO_URI", "mongodb://localhost:27017")
        self.database_name = os.getenv("DATABASE_NAME", "fonta_ai_db")
    
    async def connect(self):
        """Connect to MongoDB database."""
        try:
            self.client = AsyncIOMotorClient(self.mongo_url)
            self.database = self.client[self.database_name]
            
            # Test the connection
            await self.client.admin.command('ping')
            logger.info(f"Connected to MongoDB database: {self.database_name}")
            
        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
            raise
    
    async def disconnect(self):
        """Disconnect from MongoDB database."""
        if self.client:
            self.client.close()
            logger.info("Disconnected from MongoDB")
    
    def get_collection(self, collection_name: str):
        """Get a collection from the database."""
        if not self.database:
            raise Exception("Database not connected. Call connect() first.")
        return self.database[collection_name]

# Global database instance
database = Database()

# Collections
def get_users_collection():
    """Get users collection."""
    return database.get_collection("users")

def get_quizzes_collection():
    """Get quizzes collection."""
    return database.get_collection("quizzes")

def get_summaries_collection():
    """Get summaries collection."""
    return database.get_collection("summaries")

def get_homework_collection():
    """Get homework help collection."""
    return database.get_collection("homework_help")

def get_shared_quizzes_collection():
    """Get shared quizzes collection."""
    return database.get_collection("shared_quizzes")
