import re
from typing import List, Optional, Dict, Set

# ==================================================
# MASTER SKILL REGEX (PRE-COMPILED)
# ==================================================

RAW_SKILL_PATTERNS: Dict[str, str] = {
    "python": r"\bpython\b",
    "java": r"\bjava\b(?!\s*script)",
    "javascript": r"\b(javascript|js)\b",
    "typescript": r"\b(typescript|ts)\b",
    "sql": r"\bsql\b",
    "golang": r"\b(go|golang)\b",
    "rust": r"\brust\b",
    "cpp": r"\b(c\+\+|cpp)\b",
    "csharp": r"\b(c#|csharp|c\s*sharp)\b",
    "kotlin": r"\bkotlin\b",
    "swift": r"\bswift\b",
    "ruby": r"\bruby\b",
    "php": r"\bphp\b",
    "scala": r"\bscala\b",
    "r_lang": r"\b(r\s*(programming|language)|r-lang)\b",

    "html": r"\bhtml\d*\b",
    "css": r"\bcss\d*\b",
    "react": r"\breact(\.js|js)?\b",
    "angular": r"\bangular(\.js|js)?\b",
    "vue": r"\bvue(\.js|js)?\b",
    "nextjs": r"\bnext(\.js|js)?\b",
    "tailwind": r"\btailwind(\s*css)?\b",
    "bootstrap": r"\bbootstrap\b",
    "redux": r"\bredux\b",

    "node": r"\bnode(\.js|js)?\b",
    "express": r"\bexpress(\.js|js)?\b",
    "django": r"\bdjango\b",
    "flask": r"\bflask\b",
    "fastapi": r"\bfastapi\b",
    "spring": r"\bspring(\s*boot)?\b",

    "mongodb": r"\b(mongodb|mongo)\b",
    "postgresql": r"\b(postgresql|postgres)\b",
    "mysql": r"\bmysql\b",
    "redis": r"\bredis\b",

    "aws": r"\b(aws|amazon\s*web\s*services)\b",
    "azure": r"\b(azure|microsoft\s*azure)\b",
    "gcp": r"\b(gcp|google\s*cloud(\s*platform)?)\b",
    "docker": r"\bdocker\b",
    "kubernetes": r"\b(kubernetes|k8s)\b",
    "jenkins": r"\bjenkins\b",
    "ci_cd": r"\b(ci\s*/?\s*cd|cicd|continuous\s*(integration|deployment))\b",

    "machine_learning": r"\b(machine\s*learning|ml)\b",
    "deep_learning": r"\bdeep\s*learning\b",
    "nlp": r"\b(nlp|natural\s*language\s*processing)\b",
    "tensorflow": r"\btensorflow\b",
    "pytorch": r"\bpytorch\b",
    "scikit_learn": r"\b(scikit[\-\s]?learn|sklearn)\b",

    "git": r"\bgit\b(?!hub|lab)",
    "github": r"\bgithub\b",
    "gitlab": r"\bgitlab\b"
}

# Compile once
MASTER_SKILL_PATTERNS = {
    skill: re.compile(pattern)
    for skill, pattern in RAW_SKILL_PATTERNS.items()
}

# ==================================================
# ROLE-BASED SKILLS
# ==================================================

ROLE_SKILLS: Dict[str, Set[str]] = {
    "frontend": {
        "html", "css", "javascript", "typescript",
        "react", "vue", "angular", "nextjs",
        "tailwind", "bootstrap", "redux"
    },
    "backend": {
        "python", "java", "node", "express",
        "django", "flask", "fastapi", "spring",
        "sql", "postgresql", "mongodb", "redis"
    },
    "fullstack": {
        "html", "css", "javascript", "react",
        "node", "express", "python", "django",
        "sql", "postgresql", "mongodb", "tailwind"
    },
    "data_science": {
        "python", "sql", "machine_learning",
        "deep_learning", "nlp",
        "tensorflow", "pytorch", "scikit_learn"
    },
    "devops": {
        "docker", "kubernetes", "aws", "azure",
        "gcp", "jenkins", "ci_cd", "git"
    }
}

# ==================================================
# CORE FUNCTION
# ==================================================

def extract_skills(resume_text: str, role: Optional[str] = None) -> List[str]:
    """
    Extract skills from resume text.
    Optionally filter skills based on target role.
    """

    if not resume_text:
        return []

    resume_text = resume_text.lower()
    found_skills = set()

    for skill, pattern in MASTER_SKILL_PATTERNS.items():
        if pattern.search(resume_text):
            found_skills.add(skill)

    if role:
        role = role.lower()
        if role in ROLE_SKILLS:
            found_skills &= ROLE_SKILLS[role]

    return sorted(found_skills)
