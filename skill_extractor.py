import re

# ==================================================
# MASTER SKILL DICTIONARY (GLOBAL)
# ==================================================

MASTER_SKILL_PATTERNS = {
    # ---------- Programming Languages ----------
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

    # ---------- Frontend ----------
    "html": r"\bhtml\d*\b",
    "css": r"\bcss\d*\b",
    "react": r"\breact(\.js|js)?\b",
    "angular": r"\bangular(\.js|js)?\b",
    "vue": r"\bvue(\.js|js)?\b",
    "nextjs": r"\bnext(\.js|js)?\b",
    "tailwind": r"\btailwind(\s*css)?\b",
    "bootstrap": r"\bbootstrap\b",
    "redux": r"\bredux\b",

    # ---------- Backend ----------
    "node": r"\bnode(\.js|js)?\b",
    "express": r"\bexpress(\.js|js)?\b",
    "django": r"\bdjango\b",
    "flask": r"\bflask\b",
    "fastapi": r"\bfastapi\b",
    "spring": r"\bspring(\s*boot)?\b",

    # ---------- Databases ----------
    "mongodb": r"\b(mongodb|mongo)\b",
    "postgresql": r"\b(postgresql|postgres)\b",
    "mysql": r"\bmysql\b",
    "redis": r"\bredis\b",

    # ---------- Cloud & DevOps ----------
    "aws": r"\b(aws|amazon\s*web\s*services)\b",
    "azure": r"\b(azure|microsoft\s*azure)\b",
    "gcp": r"\b(gcp|google\s*cloud(\s*platform)?)\b",
    "docker": r"\bdocker\b",
    "kubernetes": r"\b(kubernetes|k8s)\b",
    "jenkins": r"\bjenkins\b",
    "ci_cd": r"\b(ci\s*/?\s*cd|cicd|continuous\s*(integration|deployment))\b",

    # ---------- AI / ML ----------
    "machine_learning": r"\b(machine\s*learning|ml)\b",
    "deep_learning": r"\bdeep\s*learning\b",
    "nlp": r"\b(nlp|natural\s*language\s*processing)\b",
    "tensorflow": r"\btensorflow\b",
    "pytorch": r"\bpytorch\b",
    "scikit_learn": r"\b(scikit[\-\s]?learn|sklearn)\b",

    # ---------- Version Control ----------
    "git": r"\bgit\b(?!hub|lab)",
    "github": r"\bgithub\b",
    "gitlab": r"\bgitlab\b"
}

# ==================================================
# ROLE-BASED SKILL FILTERING
# ==================================================

ROLE_SKILLS = {
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
# CORE EXTRACTION FUNCTION
# ==================================================

def extract_skills(resume_text: str, role: str = None):
    """
    Extract skills from resume text.
    If role is provided, results are filtered to role-specific skills.
    """

    resume_text = resume_text.lower()
    found_skills = set()

    for skill, pattern in MASTER_SKILL_PATTERNS.items():
        if re.search(pattern, resume_text):
            found_skills.add(skill)

    # Apply role-based filtering if role selected
    if role and role in ROLE_SKILLS:
        found_skills = found_skills.intersection(ROLE_SKILLS[role])

    return sorted(found_skills)

# ==================================================
# TESTING (DEV ONLY)
# ==================================================

# if __name__ == "__main__":
#     sample_text = """
#     alex rivera 123 tech lane, san francisco, ca 94105 (555) 012-3456 | alex.rivera.dev@email.com linkedin.com/in/alexrivera | github.com/arivera-codes professional summary dynamic and detail-oriented software engineer with over 5 years of experience in full-stack development. proven track record of optimizing system performance and leading cross-functional teams to deliver scalable web applications. passionate about ai integration and cloud-native architecture. work experience senior software engineer | techflow solutions january 2021 – present • led the migration of a legacy monolithic architecture to a microservices-based system using node.js and docker, reducing deployment time by 40%. • developed and maintained restful apis for a high-traffic e-commerce platform serving over 500k monthly active users. • mentored 4 junior developers and conducted weekly code reviews to ensure high-quality standards. junior web developer | innovate web lab june 2018 – december 2020 • collaborated with ui/ux designers to implement responsive front-end components using react.js and tailwind css. • identified and resolved 50+ critical bugs in the database layer, improving application stability by 15%. • integrated third-party payment gateways (stripe, paypal) ensuring secure transaction processing. education bachelor of science in computer science state university of technology | 2014 – 2018 • gpa: 3.8/4.0 • relevant coursework: data structures, algorithms, database management, software engineering. technical skills • languages: javascript (es6+), python, java, sql, html5, css3. • frameworks/libraries: react, node.js, express, django, redux. • tools & platforms: git, aws (ec2, s3), docker, jenkins, postgresql, mongodb. • soft skills: agile methodology, problem solving, technical documentation, team leadership. projects ai-powered task manager • built a task management tool using python and openai api to automatically prioritize user tasks based on deadlines and sentiment analysis. • deployed the application on heroku with a ci/cd pipeline.
#     """

#     print("ALL SKILLS:", extract_skills(sample_text))
#     print("BACKEND ONLY:", extract_skills(sample_text, role="backend"))
