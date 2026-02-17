# 🎯 Paraline HR AI Assistant - Complete System

**Hệ thống HR AI Assistant hoàn chỉnh với chatbot, CV screening, và job requirements management**

---

## 🌟 Overview

Paraline HR AI Assistant là hệ thống tuyển dụng tự động với 3 thành phần chính:

### 1. **HR Chatbot**
- Trả lời câu hỏi về công ty, chính sách HR
- Sử dụng ChromaDB vector database
- 440+ documents về HR policies
- Answer validation với threshold 0.7

### 2. **CV Screening System**
- Tự động phân tích và chấm điểm CV
- Parse PDF/DOCX files
- Extract skills, experience, education
- Score 0-100 với breakdown chi tiết
- Recommendations: Strong Pass / Pass / Maybe / Reject

### 3. **Job Requirements Manager**
- UI quản lý yêu cầu từng vị trí
- Customize skills, experience, scoring
- Export/Import configuration
- 11 vị trí pre-configured

---

## ✨ Features

### 🤖 HR Chatbot
- ✅ Vector-based knowledge retrieval
- ✅ Vietnamese language support
- ✅ Real-time answer validation
- ✅ Debug mode with similarity scores
- ✅ Session statistics tracking
- ✅ Professional Paraline-branded UI

### 📄 CV Upload & Processing
- ✅ Multi-format support (PDF, DOCX)
- ✅ Automatic CV storage
- ✅ Database management (JSON)
- ✅ Email notifications
- ✅ Form validation

### 🔍 AI CV Screening
- ✅ Automatic text extraction
- ✅ Skills matching (required + preferred)
- ✅ Experience detection (years)
- ✅ Education verification
- ✅ Certifications checking
- ✅ Scoring algorithm (100 points)
- ✅ Batch processing
- ✅ Export results (JSON, Excel)

### 📊 HR Dashboard
- ✅ Summary statistics
- ✅ Filter by recommendation
- ✅ Detailed score breakdown
- ✅ Quick actions (email, schedule)
- ✅ Export to Excel

### ⚙️ Job Requirements Manager
- ✅ Visual UI for HR team
- ✅ Add/Edit/Delete positions
- ✅ Customize scoring weights
- ✅ Set pass thresholds
- ✅ Export configuration

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Paraline HR System                      │
└─────────────────────────────────────────────────────────────┘
                              │
           ┌──────────────────┼──────────────────┐
           │                  │                  │
           ▼                  ▼                  ▼
    ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
    │  Chatbot    │   │ CV Upload   │   │  Screening  │
    │  Interface  │   │  & Storage  │   │   Engine    │
    └─────────────┘   └─────────────┘   └─────────────┘
           │                  │                  │
           ▼                  ▼                  ▼
    ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
    │  ChromaDB   │   │ applicants  │   │ screening   │
    │  Vector DB  │   │   _db.json  │   │ _results    │
    └─────────────┘   └─────────────┘   └─────────────┘
           │                                     │
           │                                     ▼
           │                            ┌─────────────┐
           │                            │ HR Dashboard│
           │                            └─────────────┘
           │
           ▼
    ┌─────────────┐
    │ Job Config  │
    │ Manager UI  │
    └─────────────┘
```

---

## 💻 Installation

### Prerequisites

- **Python 3.9+**
- **Windows/Linux/Mac**
- **Git**

### Step 1: Clone Repository

```bash
git clone https://github.com/your-org/hr-ai-agent-pure-vector.git
cd hr-ai-agent-pure-vector
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
# Core dependencies
pip install streamlit chromadb python-dotenv

# CV Screening dependencies
pip install PyPDF2 python-docx openpyxl pandas

# Optional: Email support
pip install smtplib
```

### Step 4: Setup Environment

```bash
# Copy example env file
cp .env.example .env

# Edit .env file
# Add your API keys, SMTP settings, etc.
```

---

## 🚀 Quick Start

### 1. Run Main Application

```bash
streamlit run streamlit_app.py
```

**Access:** http://localhost:8501

### 2. Run HR Dashboard

```bash
streamlit run hr_dashboard_page.py
```

**Access:** http://localhost:8502

### 3. Run Job Requirements Manager

```bash
streamlit run job_requirements_manager.py
```

**Access:** http://localhost:8503

### 4. Run CV Screening (CLI)

```bash
python cv_screening.py
```

---

## 📖 User Guide

### For Applicants

#### 1. Apply for Jobs

1. Visit main page: http://localhost:8501
2. Open sidebar → **💼 Ứng Tuyển Việc Làm**
3. Fill in form:
   - Họ và tên
   - Email
   - Số điện thoại
   - Vị trí ứng tuyển (dropdown)
   - Upload CV (PDF/DOCX)
4. Click **📤 Nộp Hồ Sơ**
5. Wait for confirmation ✅

#### 2. Ask HR Questions

1. Use chatbot in main interface
2. Type questions about:
   - Company policies
   - Leave policies
   - Compensation & benefits
   - Work hours
   - etc.
3. Get instant answers from knowledge base

---

### For HR Team

#### 1. Review Applications

**Via HR Dashboard:**

```bash
streamlit run hr_dashboard_page.py
```

**Features:**
- View all applicants
- See AI scores (0-100)
- Filter by recommendation:
  - ✅ Highly Recommended
  - ✅ Recommended
  - ⚠️ Consider
  - ❌ Not Recommended
- View detailed breakdown:
  - Required Skills match
  - Preferred Skills match
  - Years of experience
  - Education relevance
  - Certifications
- Quick actions:
  - 📧 Email candidate
  - 📄 View CV
  - ✅ Schedule Interview

**Via CLI:**

```bash
python cv_screening.py
```

Output:
```
🔍 CV Screening System v2
==================================================
📋 Loaded 11 positions

📊 Successfully screened 5 applicants

1. Nguyễn Văn A - Software Engineer
   Score: 78.5/100 (78.5%)
   Status: ✅ Recommended
   Action: Schedule interview
   Breakdown:
     • Required Skills: 20.0/30 (67%)
     • Preferred Skills: 15.0/20 (75%)
     • Experience: 20/25 (3 years)
     • Education: 15/15
     • Certifications: 8.5/10

✅ Results exported to: screening_results.json
```

#### 2. Manage Job Requirements

```bash
streamlit run job_requirements_manager.py
```

**Actions:**

**View Requirements:**
- Select position from dropdown
- See all details:
  - Required/Preferred skills
  - Experience requirements
  - Education requirements
  - Scoring thresholds
  - Disqualifiers

**Add New Position:**
1. Tab: **➕ Thêm/Sửa Vị Trí**
2. Mode: **Tạo mới**
3. Fill in:
   - Position name
   - Department, Level, Salary
   - Required Skills (one per line)
   - Preferred Skills (one per line)
   - Min years experience
   - Scoring thresholds
4. Click **💾 Lưu Cấu Hình**

**Edit Existing Position:**
1. Tab: **➕ Thêm/Sửa Vị Trí**
2. Mode: **Chỉnh sửa**
3. Select position
4. Modify fields
5. Click **💾 Lưu Cấu Hình**

**Export Configuration:**
- Tab: **📊 Export**
- Click **📥 Export to JSON** or **📊 Export to Excel**

#### 3. Send Interview Invitations

**Manual (Current):**
1. Note candidate email from dashboard
2. Send email manually

**Automatic (Future):**
- Configure SMTP in `.env`
- System auto-sends emails

---

## ⚙️ Configuration

### Job Requirements Configuration

**File:** `job_requirements_config.json`

**Structure:**

```json
{
  "Position Name": {
    "position_info": {
      "title": "Software Engineer",
      "department": "Engineering",
      "level": "Mid-Senior",
      "salary_range": "15-30 triệu VND"
    },
    "technical_skills": {
      "required": {
        "programming": ["Python", "JavaScript"],
        "databases": ["SQL", "PostgreSQL"]
      },
      "preferred": {
        "cloud": ["AWS", "Azure"],
        "devops": ["Docker", "Kubernetes"]
      },
      "weight": 50
    },
    "experience": {
      "min_years": 2,
      "preferred_years": 3,
      "weight": 25
    },
    "education": {
      "required_degree": "Bachelor",
      "preferred_majors": ["Computer Science", "IT"],
      "weight": 10
    },
    "certifications": {
      "preferred": ["AWS Certified Developer"],
      "weight": 5
    },
    "soft_skills": {
      "required": ["Teamwork", "Communication"],
      "weight": 10
    },
    "scoring": {
      "min_pass_score": 60,
      "excellent_score": 80,
      "auto_reject_below": 40,
      "auto_interview_above": 85
    },
    "disqualifiers": [
      "Không có kinh nghiệm lập trình"
    ]
  }
}
```

### Supported Positions (Default)

1. **Software Engineer** - Mid-Senior (60 pass score)
2. **Frontend Developer** - Junior-Mid (55 pass score)
3. **Backend Developer** - Mid-Senior (60 pass score)
4. **QA Engineer** - Junior-Mid (55 pass score)
5. **Project Manager** - Mid-Senior (65 pass score)
6. **Business Analyst** - Mid (60 pass score)
7. **HR Specialist** - Junior-Mid (55 pass score)
8. **AI Engineer** - Mid-Senior (65 pass score)
9. **AI Intern** - Intern (60 pass score)
10. **DevOps Engineer** - Mid-Senior (62 pass score)
11. **DevOps Intern** - Intern (55 pass score)

---

## 🔧 Technical Details

### Scoring Algorithm

**Total: 100 points**

| Category | Points | How it's calculated |
|----------|--------|---------------------|
| **Required Skills** | 30 | (Matched skills / Total required) × 30 |
| **Preferred Skills** | 20 | (Matched skills / Total preferred) × 20 |
| **Experience** | 25 | Based on years vs requirement |
| **Education** | 15 | 15 if relevant degree, 5 otherwise |
| **Certifications** | 10 | 5 points per cert, max 10 |

**Experience Scoring:**
- Years >= Required + 3: **25 points**
- Years >= Required: **20 points**
- Years >= Required - 1: **15 points**
- Years < Required - 1: **5 points**

**Recommendations:**
- Score >= Pass + 20: **STRONG_PASS** (✅ Highly Recommended)
- Score >= Pass: **PASS** (✅ Recommended)
- Score >= Pass - 10: **MAYBE** (⚠️ Consider)
- Score < Pass - 10: **REJECT** (❌ Not Recommended)

### CV Text Extraction

**PDF:**
```python
PyPDF2.PdfReader → Extract text from all pages
```

**DOCX:**
```python
python-docx → Extract paragraphs
```

**Supported formats:**
- ✅ .pdf
- ✅ .docx
- ✅ .doc

### Skills Matching

**Method:** Simple keyword matching (case-insensitive)

```python
# Example
cv_text = "python, javascript, react, docker"
required_skills = ["python", "javascript", "sql"]

matched = ["python", "javascript"]
percentage = 66.7%
points = 20.0 / 30
```

**Future improvement:** Use NLP/embeddings for semantic matching

### Experience Detection

**Regex patterns:**
```python
r'(\d+)\+?\s*years?\s+(?:of\s+)?experience'
r'experience.*?(\d+)\+?\s*years?'
r'(\d+)\+?\s*years?\s+in'
r'(\d+)\+?\s*năm kinh nghiệm'  # Vietnamese
```

---

## 📁 Project Structure

```
hr-ai-agent-pure-vector/
├── README.md                           ← This file
├── .env                                ← Environment variables
├── .gitignore                          ← Git ignore
├── requirements.txt                    ← Python dependencies
│
├── streamlit_app.py                    ← Main application
├── hr_dashboard_page.py                ← HR dashboard
├── job_requirements_manager.py         ← Job config manager
├── cv_screening.py                     ← CV screening engine
├── import_cvs.py                       ← Import existing CVs
├── create_sample_db.py                 ← Create sample database
│
├── src/
│   ├── services/
│   │   └── vector_db.py                ← ChromaDB service
│   └── utils/
│       └── helpers.py                  ← Helper functions
│
├── docs/
│   └── {docs,src}/                     ← Knowledge base (440 docs)
│
├── chroma_db/                          ← ChromaDB storage
│
├── cv_uploads/                         ← Uploaded CV files
│   ├── 20260215_085339_Name_CV.pdf
│   └── ...
│
├── applicants_db.json                  ← Applicant database
├── screening_results.json              ← Screening results
├── job_requirements_config.json        ← Job requirements
├── email_notifications.log             ← Email log
│
└── config/
    └── docker/
        ├── Dockerfile
        └── docker-compose.yml
```

---

## 🐛 Troubleshooting

### Common Issues

#### 1. "No applicants found in database"

**Problem:** `applicants_db.json` không tồn tại hoặc rỗng

**Solution:**
```bash
# Option A: Nộp CV qua form
streamlit run streamlit_app.py
# → Upload CV through sidebar

# Option B: Import existing CVs
python import_cvs.py

# Option C: Create sample database
python create_sample_db.py
```

#### 2. "Position not found in requirements database"

**Problem:** Vị trí trong `applicants_db.json` không có trong `job_requirements_config.json`

**Solution:**
```bash
# Add position using manager
streamlit run job_requirements_manager.py
# → Tab "➕ Thêm/Sửa"
# → Mode "Tạo mới"
# → Add position
```

#### 3. "Could not extract text from CV"

**Problem:** PDF/DOCX file bị corrupt hoặc protected

**Solution:**
- Re-save PDF using Adobe/Chrome
- Convert to new format
- Check file permissions
- Ensure file < 10MB

#### 4. Low scores for good candidates

**Problem:** Keywords không match hoặc threshold quá cao

**Solution:**
```bash
# Adjust requirements
streamlit run job_requirements_manager.py
# → Edit position
# → Lower "Min Pass Score"
# → Add more skill variations
```

#### 5. "Module not found"

**Problem:** Dependencies chưa cài

**Solution:**
```bash
pip install PyPDF2 python-docx openpyxl pandas streamlit chromadb
```

#### 6. CV files not found

**Problem:** Path in database không đúng

**Cause:** Windows vs Linux path separator (`\` vs `/`)

**Solution:** Update `applicants_db.json`:
```json
{
  "cv_path": "cv_uploads/20260215_file.pdf"  // Use /
}
```

---

## 📊 Data Flow

### 1. Application Submission

```
User fills form
     ↓
streamlit_app.py validates input
     ↓
save_cv_to_disk() → cv_uploads/TIMESTAMP_NAME_FILE.pdf
     ↓
save_to_database() → applicants_db.json
     ↓
send_email_notification() → email_notifications.log
     ↓
Display success ✅
```

### 2. CV Screening

```
HR runs cv_screening.py
     ↓
load_job_requirements() → Read job_requirements_config.json
     ↓
screen_all_applicants() → Read applicants_db.json
     ↓
For each applicant:
  - extract_cv_text() → Parse PDF/DOCX
  - score_cv() → Calculate score
  - return result
     ↓
Sort by score (highest first)
     ↓
export_screening_results() → screening_results.json
```

### 3. HR Dashboard View

```
HR opens hr_dashboard_page.py
     ↓
Load screening_results.json
     ↓
Display summary stats
     ↓
Filter by recommendation
     ↓
Show detailed breakdown
     ↓
Quick actions (email, schedule)
```

---

## 🔐 Security Considerations

### Current Implementation

- ✅ Files stored locally
- ✅ No authentication (local use only)
- ✅ No database encryption
- ✅ Email logs only (no actual sending)

### Production Recommendations

1. **Authentication:**
   - Add login system (Streamlit Auth)
   - Role-based access (HR vs Applicant)
   - Session management

2. **Data Encryption:**
   - Encrypt `applicants_db.json`
   - Secure CV files
   - HTTPS for web access

3. **Database:**
   - Move to PostgreSQL
   - Use proper ORM (SQLAlchemy)
   - Database backups

4. **Email:**
   - Configure SMTP securely
   - Use email templates
   - Queue system for bulk emails

5. **File Storage:**
   - Use cloud storage (S3, GCS)
   - Virus scanning
   - Access control

6. **API Security:**
   - Rate limiting
   - Input validation
   - CORS configuration

---

## 📈 Performance

### Current Metrics

| Operation | Time | Notes |
|-----------|------|-------|
| CV Upload | < 1s | Local disk |
| PDF Parsing | 1-3s | Depends on size |
| CV Scoring | < 1s | Per CV |
| Batch Screening (10 CVs) | ~10s | Sequential |
| Dashboard Load | < 2s | JSON read |
| Chatbot Query | 0.5-1s | Vector search |

### Optimization Tips

1. **Batch Processing:**
   - Use multiprocessing for parallel CV screening
   - Current: Sequential
   - Improved: Process 4-8 CVs simultaneously

2. **Caching:**
   - Cache parsed CV text
   - Cache screening results
   - Use Redis for production

3. **Database:**
   - Move to PostgreSQL
   - Index on position, score
   - Pagination for large datasets

---

## 🚀 Future Enhancements

### Phase 1: Core Improvements

- [ ] **AI-Powered CV Analysis**
  - Use Claude/GPT API for better parsing
  - Semantic skill matching
  - Extract soft skills
  - Understand job descriptions

- [ ] **Email Automation**
  - SMTP configuration
  - Email templates
  - Auto-send interview invitations
  - Auto-send rejections

- [ ] **Calendar Integration**
  - Google Calendar API
  - Auto-schedule interviews
  - Send calendar invites
  - Reminder system

### Phase 2: Advanced Features

- [ ] **Interview Management**
  - Track interview stages
  - Interviewer feedback forms
  - Decision tracking
  - Offer management

- [ ] **Analytics Dashboard**
  - Time-to-hire metrics
  - Source tracking (LinkedIn, etc.)
  - Conversion rates
  - Hiring pipeline visualization

- [ ] **Candidate Portal**
  - Check application status
  - Update documents
  - Schedule interviews
  - Receive notifications

### Phase 3: Enterprise Features

- [ ] **Multi-tenancy**
  - Support multiple companies
  - Separate databases
  - Custom branding

- [ ] **ATS Integration**
  - Integrate with existing ATS
  - API for external systems
  - Webhook support

- [ ] **Machine Learning**
  - Learn from past hiring decisions
  - Improve scoring accuracy
  - Predict candidate success
  - Bias detection

- [ ] **Compliance**
  - GDPR compliance
  - Data retention policies
  - Audit logs
  - Privacy controls

---

## 🤝 Contributing

### Development Setup

```bash
# Fork repo
git clone https://github.com/your-username/hr-ai-agent-pure-vector.git

# Create branch
git checkout -b feature/your-feature

# Make changes
# Test thoroughly

# Commit
git commit -m "Add: your feature"

# Push
git push origin feature/your-feature

# Create Pull Request
```

### Code Standards

- Python 3.9+
- PEP 8 style guide
- Type hints
- Docstrings for functions
- Unit tests for core logic

---

## 📝 Changelog

### v2.0.0 (2026-02-16)
- ✅ Added CV screening system
- ✅ Added HR dashboard
- ✅ Added job requirements manager
- ✅ Support 11 positions
- ✅ Configurable scoring
- ✅ Export to Excel

### v1.0.0 (2026-02-15)
- ✅ Initial release
- ✅ HR Chatbot
- ✅ CV upload form
- ✅ ChromaDB integration
- ✅ Paraline branding

---

## 📄 License

MIT License - See LICENSE file for details

---

## 👥 Team

**Paraline Software**
- 📧 Email: info@paraline.com.vn
- 📞 Phone: +84 24-3200-4679
- 🌐 Website: https://paraline.com.vn

---

## 🙏 Acknowledgments

- Streamlit for amazing UI framework
- ChromaDB for vector database
- PyPDF2 & python-docx for document parsing
- Claude AI for development assistance

---

## 📞 Support

### Documentation
- [Installation Guide](docs/installation.md)
- [User Manual](docs/user-manual.md)
- [API Reference](docs/api-reference.md)

### Contact
- **Email:** hr@paraline.com.vn
- **GitHub Issues:** https://github.com/your-org/hr-ai-agent/issues

---

**Made with ❤️ in Hanoi, Vietnam**

© 2017-2026 Paraline Software. Japan Quality in Vietnam.