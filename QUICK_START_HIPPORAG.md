# 🚀 Quick Start - HippoRAG Version

## ⚡ 5-Minute Setup

### 1. Extract & Install
```bash
tar -xzf hr-ai-agent-hipporag.tar.gz
cd hr-ai-agent-hipporag
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 2. Add API Key
```bash
cp config/.env.example .env
# Edit: GOOGLE_API_KEY=your-key-here
```

### 3. Prepare Sample Document

Create `documents/sample_questions.md`:

```markdown
# Backend Developer Questions

## Question: REST API
**Difficulty:** Medium
**Question:** Explain REST API principles
**Expected Answer:** REST uses HTTP methods, stateless, resources

## Question: Database
**Difficulty:** High  
**Question:** Explain database indexing
**Expected Answer:** Indexes speed up queries, trade-off with write speed
```

### 4. Index Documents
```bash
python scripts/ingest_documents.py
```

### 5. Run!
```bash
streamlit run streamlit_app_v2.py
```

## 🎯 What's Different?

**Before:** Questions hard-coded in Python
**Now:** Questions from your documents!

Just upload PDF → Auto-indexed → Ready to use!

## 📊 Key Benefits

✅ Upload PDF = Add 100 questions (5 mins)
✅ Update document = Update questions (no code!)
✅ Scale to 1000+ questions easily
✅ Intelligent retrieval with knowledge graph

## 🔧 Daily Use

### Add New Questions:
1. Edit your document or create new PDF
2. Run: `python scripts/ingest_documents.py`
3. Done! New questions available immediately

### Update Questions:
1. Modify document
2. Re-index
3. Changes reflected

No code changes, no deployment needed!

---

**Time to Production:** 5 minutes
**Learning Curve:** Low (if you know how to create documents)
**Maintenance:** Minimal (edit documents, not code)
