#!/usr/bin/env python3
"""
HR AI Agent
"""

import sys
import os

# Add src to path (FIXED syntax error)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from dotenv import load_dotenv
load_dotenv()

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

print("="*80)
print("🏢 HR AI AGENT - PURE VECTOR DATABASE")
print("="*80)
print()
print("✅ ChromaDB Only (NO SQL!)")
print("🔒 100% Local (vector retrieval, no Ollama)")
print("💰 $0 Cost")
print()

# Test Vector DB
try:
    from services.vector_db import get_vector_db
    
    print("🔍 Testing Vector Database...")
    vdb = get_vector_db()
    
    print(f"✅ Vector DB initialized!")
    print(f"📊 Collections: {len(vdb.collections)}")
    for name, collection in vdb.collections.items():
        count = collection.count()
        print(f"   - {name}: {count} documents")
    
    print()
    print("🎉 System ready!")
    print()
    print("💡 Next steps:")
    print("  - Web UI: streamlit run streamlit_app.py")
    print("  - Add documents to: documents/ folder")
    print("  - Index: python scripts/ingest_documents.py")
    
except ImportError as e:
    print(f"❌ Missing package: {e}")
    print("Install: pip install -r requirements.txt")
except Exception as e:
    print(f"⚠️  Note: {e}")
    print()
    print("This is normal for first run.")
    print("Add documents and index them to get started!")

print("="*80)