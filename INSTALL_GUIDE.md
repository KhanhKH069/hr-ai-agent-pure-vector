# 📦 Installation Guide - Offline Version

## ⏱️ 10-Minute Setup

### 1. Install Ollama (2 mins)

**Mac:**
```bash
brew install ollama
```

**Linux:**
```bash
curl https://ollama.ai/install.sh | sh
```

**Windows:**
1. Download from [ollama.ai](https://ollama.ai)
2. Run installer
3. Done!

### 2. Download Model (5 mins)

```bash
# Start Ollama
ollama serve

# In another terminal:
ollama pull llama3.2
# Downloads ~2GB
```

### 3. Extract Project (1 min)

```bash
tar -xzf hr-ai-agent-offline.tar.gz
cd hr-ai-agent-offline
```

### 4. Install Python Packages (2 mins)

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 5. Test! (30 seconds)

```bash
# Make sure Ollama is running
ollama serve

# In another terminal:
python main.py
```

Should see:
```
🏢 HR AI AGENT - OFFLINE
✅ Ollama connected
✅ Ready!
```

**Done! Now disconnect internet and test again!** ✅

---

## 🎯 Quick Test

```bash
# Disconnect WiFi

# Test console
python main.py
"Công ty có bao nhiêu ngày phép?"
# Works! ✅

# Test Streamlit
streamlit run streamlit_app.py
# Works! ✅
```

---

## 📝 Adding Your Documents

```bash
# 1. Put PDFs in documents/
cp your_questions.pdf documents/

# 2. Index (works offline!)
python scripts/ingest_documents.py

# 3. Done!
```

---

## 🚀 Daily Use

```bash
# Start Ollama (once per reboot)
ollama serve

# Run app
streamlit run streamlit_app.py

# Or console
python main.py
```

**No internet needed after initial setup!** 🔒
