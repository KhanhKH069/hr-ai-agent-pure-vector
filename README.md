# 🎯 Paraline HR AI Assistant

**Hệ thống tuyển dụng thông minh với AI chatbot, CV screening tự động, và quản lý job requirements**

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.32-red.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Mục Lục

- [Tổng Quan](#tổng-quan)
- [Tính Năng](#tính-năng)
- [Cài Đặt](#cài-đặt)
- [Sử Dụng](#sử-dụng)
- [Cấu Hình](#cấu-hình)
- [Hướng Dẫn Chi Tiết](#hướng-dẫn-chi-tiết)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)

---

## 🌟 Tổng Quan

Paraline HR AI Assistant bao gồm **3 thành phần chính**:

### **1. 🤖 HR Chatbot**
Trả lời tự động câu hỏi về công ty, chính sách HR
- 440+ tài liệu HR policies
- ChromaDB vector database
- Hỗ trợ tiếng Việt
- Real-time search

### **2. 📄 CV Screening System**
Phân tích và chấm điểm CV tự động
- Parse PDF/DOCX
- Extract skills, experience, education
- Scoring 0-100 points
- Export Excel reports

### **3. ⚙️ Job Requirements Manager**
Quản lý yêu cầu tuyển dụng
- 11 vị trí pre-configured
- Customize skills & scoring
- Import/Export config

---

## ✨ Tính Năng

### Cho Ứng Viên
- ✅ Upload CV (PDF, DOCX)
- ✅ Hỏi đáp với chatbot về công ty
- ✅ Nộp đơn ứng tuyển online

### Cho HR Team
- ✅ Tự động screening CV (100 điểm)
- ✅ Dashboard xem kết quả
- ✅ Filter theo đề xuất (Pass/Reject)
- ✅ Chi tiết breakdown từng CV
- ✅ Export Excel
- ✅ Quản lý job requirements

---

## 💻 Cài Đặt

### Yêu Cầu
- Python 3.9+
- pip
- 2GB RAM
- Windows/Linux/Mac

### Bước 1: Clone Project

```bash
git clone https://github.com/your-org/hr-ai-agent.git
cd hr-ai-agent
```

### Bước 2: Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### Bước 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies chính:**
```txt
streamlit==1.32.0          # Web UI
chromadb==0.4.22           # Vector database
sentence-transformers==2.7.0  # Embeddings
PyPDF2==3.0.1              # PDF parsing
python-docx==1.1.0         # DOCX parsing
pandas==2.2.0              # Data processing
openpyxl==3.1.2            # Excel export
```

### Bước 4: Setup (Optional)

```bash
# Copy environment template
cp .env.example .env

# Edit if needed (SMTP, etc.)
```

---

## 🚀 Sử Dụng

### 1. Main App (Chatbot + CV Upload)

```bash
streamlit run streamlit_app.py
```

**Truy cập:** http://localhost:8501

**Features:**
- Chatbot trả lời câu hỏi HR
- Form upload CV
- Sidebar ứng tuyển

### 2. HR Dashboard

```bash
streamlit run hr_dashboard_page.py
```

**Truy cập:** http://localhost:8502

**Features:**
- Xem tất cả ứng viên
- Filter theo recommendation
- Score breakdown chi tiết
- Export Excel

### 3. Job Requirements Manager

```bash
streamlit run job_requirements_manager.py
```

**Truy cập:** http://localhost:8503

**Features:**
- Add/Edit positions
- Customize skills
- Set pass thresholds

### 4. CV Screening (CLI)

```bash
python cv_screening.py
```

**Output:**
```
🔍 CV Screening System
==================================================
📊 Screened 5 applicants

1. Nguyễn Văn A - Software Engineer
   Score: 78.5/100 (78.5%)
   Status: ✅ Recommended
   
✅ Results exported to: screening_results.json
```

---

## ⚙️ Cấu Hình

### Job Requirements

**File:** `job_requirements_config.json`

**11 vị trí mặc định:**
1. Software Engineer
2. Frontend Developer
3. Backend Developer
4. QA Engineer
5. Project Manager
6. Business Analyst
7. HR Specialist
8. AI Engineer
9. AI Intern
10. DevOps Engineer
11. DevOps Intern

**Cấu trúc:**

```json
{
  "Software Engineer": {
    "technical_skills": {
      "required": {
        "programming": ["Python", "JavaScript"],
        "databases": ["SQL"]
      },
      "preferred": {
        "cloud": ["AWS", "Docker"]
      }
    },
    "experience": {
      "min_years": 2
    },
    "scoring": {
      "min_pass_score": 60
    }
  }
}
```

**Customize qua UI:**
```bash
streamlit run job_requirements_manager.py
```

---

## 📖 Hướng Dẫn Chi Tiết

### Cho Ứng Viên

**Nộp CV:**
1. Vào http://localhost:8501
2. Sidebar → **💼 Ứng Tuyển Việc Làm**
3. Điền form:
   - Họ tên
   - Email
   - Số điện thoại
   - Chọn vị trí
   - Upload CV (PDF/DOCX, max 10MB)
4. Click **📤 Nộp Hồ Sơ**

**Hỏi chatbot:**
- "Nghỉ phép mấy ngày?"
- "Giờ làm việc?"
- "Lương trả khi nào?"

---

### Cho HR Team

**Review CV:**

**Option A: Dashboard**
```bash
streamlit run hr_dashboard_page.py
```
- Xem summary stats
- Filter: Highly Recommended / Recommended / Consider / Reject
- View breakdown chi tiết
- Export Excel

**Option B: CLI**
```bash
python cv_screening.py
```
- Batch process tất cả CV
- Output terminal
- Export JSON

**Quản lý positions:**
```bash
streamlit run job_requirements_manager.py
```
- Tab 1: View requirements
- Tab 2: Add/Edit position
- Tab 3: Export config

---

## 🔧 Scoring Algorithm

**Total: 100 điểm**

| Category | Points | Calculation |
|----------|--------|-------------|
| Required Skills | 30 | (Matched/Total) × 30 |
| Preferred Skills | 20 | (Matched/Total) × 20 |
| Experience | 25 | Theo năm kinh nghiệm |
| Education | 15 | 15 nếu đúng ngành, 5 nếu không |
| Certifications | 10 | 5 điểm/cert, max 10 |

**Experience scoring:**
```
Years >= Required + 3: 25 pts
Years >= Required:     20 pts
Years >= Required - 1: 15 pts
Years < Required - 1:   5 pts
```

**Recommendations:**
```
Score >= Pass + 20: ⭐ STRONG_PASS (Highly Recommended)
Score >= Pass:      ✅ PASS (Recommended)
Score >= Pass - 10: ⚠️ MAYBE (Consider)
Score < Pass - 10:  ❌ REJECT (Not Recommended)
```

---

## 📁 Cấu Trúc Project

```
hr-ai-agent-pure-vector/
│
├── README.md                        ← Bạn đang đọc
├── requirements.txt                 ← Dependencies
├── .env.example                     ← Environment template
│
├── streamlit_app.py                 ← Main app (chatbot + CV upload)
├── hr_dashboard_page.py             ← HR dashboard
├── job_requirements_manager.py      ← Job config manager
├── cv_screening.py                  ← CV screening engine
│
├── src/
│   └── services/
│       └── vector_db.py             ← ChromaDB wrapper
│
├── docs/                            ← Knowledge base (440 files)
├── chroma_db/                       ← Vector database storage
├── cv_uploads/                      ← Uploaded CV files
│
├── applicants_db.json               ← Applicant database
├── screening_results.json           ← Screening output
├── job_requirements_config.json     ← Job requirements
└── email_notifications.log          ← Email log
```

---

## 🐛 Troubleshooting

### 1. "No applicants found"

**Nguyên nhân:** Database rỗng

**Giải pháp:**
```bash
# Nộp CV qua form hoặc
python create_sample_db.py
```

### 2. "Position not found"

**Nguyên nhân:** Vị trí trong DB không có trong config

**Giải pháp:**
```bash
streamlit run job_requirements_manager.py
# → Thêm vị trí mới
```

### 3. "Could not extract text from CV"

**Nguyên nhân:** PDF corrupt hoặc protected

**Giải pháp:**
- Re-save PDF
- Remove password
- Check file size < 10MB

### 4. "Module not found"

**Giải pháp:**
```bash
pip install -r requirements.txt
```

### 5. Chatbot không trả lời

**Nguyên nhân:** Chưa build knowledge base

**Giải pháp:**
```bash
# Rebuild vector database
python rebuild_knowledge_base.py
```

### 6. Lỗi chữ trắng trong chatbot

**Giải pháp:** Xem file `fix_white_text.txt`

---

## 📊 Performance

| Task | Time | Notes |
|------|------|-------|
| CV Upload | < 1s | Local storage |
| PDF Parsing | 1-3s | Depends on size |
| CV Scoring | < 1s | Per CV |
| Batch (10 CVs) | ~10s | Sequential |
| Chatbot Query | 0.5-1s | Vector search |

**Optimization:**
- Parallel processing cho batch screening
- Cache parsed CV text
- PostgreSQL cho production

---

## 🗺️ Roadmap

### Phase 1: Current ✅
- HR Chatbot
- CV screening (100 điểm)
- Dashboard
- Job manager

### Phase 2: Next Steps
- [ ] Email automation (SMTP)
- [ ] Calendar integration (Google Calendar)
- [ ] Advanced NLP parsing
- [ ] Multi-language support

### Phase 3: Future
- [ ] Interview management
- [ ] Analytics dashboard
- [ ] ATS integration
- [ ] Mobile app
- [ ] AI-powered matching

---

## 🔐 Security Notes

**Current (Development):**
- Local file storage
- No authentication
- JSON database
- Email logging only

**Production Recommendations:**
- Add authentication (Streamlit Auth)
- Encrypt sensitive data
- Use PostgreSQL
- Configure SMTP
- Cloud storage (S3/GCS)
- HTTPS
- Rate limiting

---

## 📝 Changelog

### v2.0.0 (2026-02-20)
- ✅ CV screening system
- ✅ HR dashboard
- ✅ Job requirements manager
- ✅ 11 positions
- ✅ Excel export

### v1.0.0 (2026-02-15)
- ✅ HR Chatbot
- ✅ CV upload
- ✅ ChromaDB integration

---

## 🤝 Contributing

```bash
# Fork & clone
git clone https://github.com/your-username/hr-ai-agent.git

# Create branch
git checkout -b feature/your-feature

# Make changes & test
pytest tests/

# Commit & push
git commit -m "Add: feature"
git push origin feature/your-feature

# Create PR
```

**Code Standards:**
- Python 3.9+
- PEP 8
- Type hints
- Docstrings

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file

---

## 👥 Team & Contact

**Paraline Software**

- 🌐 Website: https://paraline.com.vn
- 📧 Email: info@paraline.com.vn
- 📞 Phone: +84 24-3200-4679
- 📍 Hanoi, Vietnam

**Support:**
- Email: hr@paraline.com.vn
- GitHub Issues: [Report Bug](https://github.com/your-org/hr-ai-agent/issues)

---

## 🙏 Acknowledgments

- **Streamlit** - Web framework
- **ChromaDB** - Vector database
- **PyPDF2** & **python-docx** - Document parsing
- **Claude AI** - Development assistance

---

## 📚 Documentation

- [Installation Guide](docs/installation.md)
- [User Manual](docs/user-manual.md)
- [API Reference](docs/api-reference.md)
- [LangChain Migration](LANGCHAIN_V1_MIGRATION_GUIDE.md)

---

## ⭐ Quick Start Summary

```bash
# 1. Install
pip install -r requirements.txt

# 2. Run main app
streamlit run streamlit_app.py
# → http://localhost:8501

# 3. Run dashboard
streamlit run hr_dashboard_page.py
# → http://localhost:8502

# 4. Screen CVs
python cv_screening.py
```

---

**Made with ❤️ in Hanoi, Vietnam**

**© 2017-2026 Paraline Software • Japan Quality in Vietnam**

---

## 🎯 Key Features Summary

| Feature | Status | Description |
|---------|--------|-------------|
| HR Chatbot | ✅ | 440+ docs, Vietnamese support |
| CV Upload | ✅ | PDF/DOCX, auto-storage |
| CV Screening | ✅ | 100-point scoring |
| Dashboard | ✅ | Filter, export Excel |
| Job Manager | ✅ | 11 positions, customizable |
| Email Notify | 🔄 | Log only (SMTP coming) |
| Analytics | 📅 | Planned |
| Mobile | 📅 | Planned |

**Legend:** ✅ Done | 🔄 In Progress | 📅 Planned

---

**⭐ Star this repo if you find it useful!**

**🐛 Found a bug? [Report it](https://github.com/your-org/hr-ai-agent/issues)**