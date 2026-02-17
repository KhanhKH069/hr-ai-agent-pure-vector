"""
Pure Vector Database - NO SQL!
Everything stored in ChromaDB collections
"""

import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import os
from datetime import datetime
from typing import List, Dict, Optional
import logging

logger = logging.getLogger(__name__)

class VectorDatabase:
    """Pure ChromaDB storage - NO SQL anywhere!"""
    
    def __init__(self, persist_directory: str = "./chroma_db"):
        logger.info("🚀 Initializing PURE Vector Database (NO SQL)")
        
        # ChromaDB client with telemetry DISABLED
        self.client = chromadb.PersistentClient(
            path=persist_directory,
            settings=Settings(
                anonymized_telemetry=False,  # ✅ FIXED: Disable telemetry warnings
                allow_reset=True
            )
        )
        
        # Local embeddings
        model_name = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
        self.embedder = SentenceTransformer(model_name)
        logger.info(f"📊 Embedding model: {model_name}")
        
        # Collections (instead of SQL tables!)
        self.collections = {}
        self._init_collections()
        
        logger.info(f"✅ Vector DB ready with {len(self.collections)} collections (NO SQL!)")
    
    def _init_collections(self):
        """Initialize all collections"""
        collection_names = [
            'interview_questions',
            'hr_policies',
            'onboarding_procedures',
            'candidate_results',
            'audit_logs'
        ]
        
        for name in collection_names:
            try:
                self.collections[name] = self.client.get_collection(name)
                logger.info(f"  ✅ Loaded collection: {name}")
            except:
                self.collections[name] = self.client.create_collection(
                    name=name,
                    metadata={"description": f"Collection for {name}"}
                )
                logger.info(f"  🆕 Created collection: {name}")
    
    def add(self, collection_name: str, documents: List[str], 
            metadatas: List[Dict], ids: Optional[List[str]] = None):
        """Add documents to collection"""
        
        if collection_name not in self.collections:
            raise ValueError(f"Collection {collection_name} not found")
        
        collection = self.collections[collection_name]
        
        # Generate embeddings
        embeddings = self.embedder.encode(documents).tolist()
        
        # Auto-generate IDs if needed
        if ids is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            ids = [f"{collection_name}_{timestamp}_{i}" for i in range(len(documents))]
        
        # Add to ChromaDB
        collection.add(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )
        
        logger.info(f"✅ Added {len(documents)} docs to {collection_name}")
        return ids
    
    def query(self, collection_name: str, query_text: str, 
             n_results: int = 10, where: Optional[Dict] = None):
        """Vector similarity search"""
        
        collection = self.collections[collection_name]
        
        # Generate query embedding
        query_embedding = self.embedder.encode([query_text]).tolist()
        
        # Search
        results = collection.query(
            query_embeddings=query_embedding,
            n_results=n_results,
            where=where
        )
        
        return results
    
    def get(self, collection_name: str, where: Optional[Dict] = None, 
            ids: Optional[List[str]] = None, limit: Optional[int] = None):
        """Get documents by filter or ID"""
        
        collection = self.collections[collection_name]
        return collection.get(where=where, ids=ids, limit=limit)
    
    def delete(self, collection_name: str, ids: List[str]):
        """Delete documents"""
        collection = self.collections[collection_name]
        collection.delete(ids=ids)
        logger.info(f"🗑️  Deleted {len(ids)} docs from {collection_name}")
    
    def count(self, collection_name: str) -> int:
        """Count documents"""
        return self.collections[collection_name].count()

# Global instance
_vector_db = None

def get_vector_db() -> VectorDatabase:
    """Get singleton instance"""
    global _vector_db
    if _vector_db is None:
        persist_dir = os.getenv("CHROMA_DB_PATH", "./chroma_db")
        _vector_db = VectorDatabase(persist_dir)
    return _vector_db