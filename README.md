# 🧠 AI Resume Analyzer & Skill Gap Finder

A **rule-based AI Resume Analyzer** that extracts skills from resumes, compares them against role-specific requirements, calculates a **weighted match score**, and generates **actionable improvement recommendations**.

Built with **Python**, designed with **real hiring logic**, not buzzwords.

---

## 🚀 Features

### ✅ Resume Skill Extraction
- Extracts technical skills from PDF resumes using regex-based matching
- Handles noisy text and formatting issues
- Avoids false positives (e.g. `Java` vs `JavaScript`)

---

### 🎯 Role-Based Skill Analysis
Supports predefined roles:
- Frontend Developer
- Backend Developer
- Full Stack Developer
- Data Science
- DevOps

Each role has its **own required skill set**.

---

### 📊 Weighted Skill Match Scoring
Unlike simple percentage matching, this project:
- Assigns **priority weights** to skills  
  - Critical → 3  
  - High → 2  
  - Medium → 1  
- Calculates a **realistic match percentage**
- Reflects how recruiters actually evaluate resumes

---

### 🧩 Skill Gap Identification
Clearly separates:
- ✅ Matched skills
- ❌ Missing skills
- ➕ Extra skills (not required but useful)

Missing skills are grouped by **priority level**.

---

### 🧭 Smart Recommendations
Generates human-readable suggestions like:
- 🚨 Skills to learn immediately
- 📈 Skills that strengthen the profile
- ✅ Confirmation when requirements are met

---

### 🛣 Learning Roadmap Generator
Creates a structured roadmap for any role:
- Fundamentals
- Intermediate
- Advanced

---

### 🔄 Multi-Role Comparison
Compares a resume against **all roles** and ranks them to find:
- Best matching role
- Match percentages for all roles

---

## 🏗 Project Structure

ai-resume-analyzer/
│
├── resume_parser.py # Extracts raw text from PDF resumes
├── skill_extractor.py # Skill detection + role-based filtering
├── skill_gap.py # Analysis, scoring, recommendations & roadmap
└── README.md

---

## ⚙️ How It Works (Pipeline)

1. Extract text from resume (PDF)
2. Detect skills using regex patterns
3. Compare skills with role requirements
4. Apply weighted scoring
5. Identify gaps and priorities
6. Generate recommendations and roadmap

---

## 🧪 Example Usage

```python
from resume_parser import extract_text_from_resume
from skill_gap import analyze_skill_gap, compare_multiple_roles

resume_text = extract_text_from_resume("sample_resume.pdf")

analysis = analyze_skill_gap(
    resume_text=resume_text,
    role="backend",
    include_resources=True
)

print(analysis)
---

## Sample Output

{
  "role": "backend",
  "match_percentage": 72.5,
  "rating": "Good ⭐⭐⭐",
  "matched_skills": ["python", "sql", "django"],
  "missing_skills": ["docker", "aws"],
  "priority_breakdown": {
    "critical": ["docker", "aws"],
    "high": [],
    "medium": [],
    "low": []
  },
  "recommendations": [
    "🚨 Focus immediately on core backend skills: docker, aws"
  ]
}
```


## 🧠 Why This Project Is Different

❌ No black-box AI hype

✅ Transparent, explainable logic

✅ Interview-friendly architecture

✅ Easy to extend with ML later

✅ Designed like a real hiring tool

🛠 Tech Stack

Python 3

pdfplumber

Regular Expressions

Typed functions & modular design

🔮 Future Improvements

Resume section weighting (Experience > Projects > Skills)

Skill proficiency detection

Job description comparison

Web UI (Streamlit / Flask)

ML-based skill inference (Phase 2)

👨‍💻 Author

Jyotirmoy Laha
BCA Student | Aspiring Software Engineer

📧 Email: jyotirmoylaha713128@gmail.com

🌐 Portfolio: https://ai-resume-analyzer-hhhb.onrender.com
