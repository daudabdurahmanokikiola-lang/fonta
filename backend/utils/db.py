# ===========================================
# FONTA AI STUDY COMPANION - DATABASE UTILITIES
# ===========================================

"""
MongoDB database connection and utilities.
Manages connections to MongoDB Atlas and provides collection access.
"""

import os
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class DatabaseManager:
    """MongoDB database manager."""

    def __init__(self):
        self.client: Optional[MongoClient] = None
        self.db: Optional[Database] = None
        self.mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
        self.db_name = os.getenv("DATABASE_NAME", "fonta_ai_db")

    def connect(self):
        """Connect to MongoDB database."""
        try:
            self.client = MongoClient(self.mongo_uri)
            self.db = self.client[self.db_name]

            # Test the connection
            self.client.admin.command('ping')
            logger.info(f"Connected to MongoDB database: {self.db_name}")

        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
            raise

    def disconnect(self):
        """Disconnect from MongoDB database."""
        if self.client:
            self.client.close()
            logger.info("Disconnected from MongoDB")

    def get_collection(self, collection_name: str) -> Collection:
        """Get a collection from the database."""
        if not self.db:
            raise Exception("Database not connected. Call connect() first.")
        return self.db[collection_name]

# Global database instance
db_manager = DatabaseManager()

# Collection accessors
def get_users_collection() -> Collection:
    """Get users collection."""
    return db_manager.get_collection("users")

def get_summaries_collection() -> Collection:
    """Get summaries collection."""
    return db_manager.get_collection("summaries")

def get_quizzes_collection() -> Collection:
    """Get quizzes collection."""
    return db_manager.get_collection("quizzes")

def get_homework_collection() -> Collection:
    """Get homework requests collection."""
    return db_manager.get_collection("homework_requests")
