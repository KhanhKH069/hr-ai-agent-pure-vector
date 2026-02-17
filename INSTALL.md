# 📦 Installation Guide - Offline Version

## ⚡ Quick Install (5 Steps)

### 1. Install Ollama

**Mac:**
```bash
curl https://ollama.ai/install.sh | sh
```

**Linux:**
```bash
curl https://ollama.ai/install.sh | sh
```

**Windows:**
Download: https://ollama.ai/download/windows

### 2. Download Model

```bash
ollama pull llama3.2:3b
```

Wait ~2 minutes for download.

### 3. Extract Project

```bash
tar -xzf hr-ai-agent-offline.tar.gz
cd hr-ai-agent-offline
```

### 4. Install Python Packages

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 5. Run!

```bash
# Start Ollama (in separate terminal)
ollama serve

# Run application
streamlit run streamlit_app_v2.py
```

**DONE!** ✅ No API key needed!

---

## 🔍 Verify Installation

```bash
python check_offline.py
```

Should show:
```
✅ Ollama: Running
✅ Model: llama3.2:3b available
✅ Embeddings: all-MiniLM-L6-v2 ready
✅ ChromaDB: Ready
✅ All systems OFFLINE and ready!
```

---

## 🐛 Common Issues

### "Ollama not found"

```bash
# Check installation
which ollama

# Reinstall if needed
curl https://ollama.ai/install.sh | sh
```

### "Model not downloaded"

```bash
ollama list
# If empty:
ollama pull llama3.2:3b
```

### "Python package errors"

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Reinstall
pip install -r requirements.txt
```

---

**Total Time:** 10-15 minutes
**Disk Space:** ~5GB
**Internet:** Only for initial download
