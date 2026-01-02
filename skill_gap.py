from typing import Dict, List, Set, Any
from skill_extractor import extract_skills, ROLE_SKILLS

# ==================================================
# SKILL PRIORITY LEVELS
# ==================================================

SKILL_PRIORITY: Dict[str, str] = {
    # Core Languages
    "python": "critical",
    "java": "critical",
    "javascript": "critical",
    "sql": "critical",

    # Frontend
    "html": "critical",
    "css": "critical",
    "react": "critical",
    "typescript": "high",
    "nextjs": "high",
    "tailwind": "medium",
    "redux": "medium",

    # Backend
    "node": "critical",
    "express": "high",
    "django": "high",
    "fastapi": "medium",
    "postgresql": "high",
    "mongodb": "high",
    "redis": "medium",

    # DevOps
    "docker": "critical",
    "aws": "critical",
    "git": "critical",
    "kubernetes": "high",
    "ci_cd": "high",

    # Data / AI
    "machine_learning": "critical",
    "pandas": "critical",
    "numpy": "high",
    "deep_learning": "high",
    "nlp": "high"
}

# ==================================================
# OPTIONAL LEARNING RESOURCES
# ==================================================

LEARNING_RESOURCES: Dict[str, str] = {
    "python": "https://www.python.org/about/gettingstarted/",
    "javascript": "https://javascript.info/",
    "react": "https://react.dev/learn",
    "node": "https://nodejs.org/en/learn",
    "docker": "https://docs.docker.com/get-started/",
    "aws": "https://aws.amazon.com/training/",
    "sql": "https://www.w3schools.com/sql/",
    "django": "https://docs.djangoproject.com/en/stable/intro/",
    "fastapi": "https://fastapi.tiangolo.com/tutorial/",
    "postgresql": "https://www.postgresql.org/docs/current/tutorial.html"
}

# ==================================================
# CORE SKILL GAP ANALYSIS
# ==================================================

def analyze_skill_gap(
    resume_text: str,
    role: str,
    include_resources: bool = False
) -> Dict[str, Any]:
    """
    Analyze skill match between resume and target role.
    """

    # ---------- Input Validation ----------
    if not resume_text or not isinstance(resume_text, str):
        raise ValueError("resume_text must be a non-empty string")

    role = role.lower().strip()
    if role not in ROLE_SKILLS:
        raise ValueError(
            f"Invalid role '{role}'. Available roles: {list(ROLE_SKILLS.keys())}"
        )

    # ---------- Skill Extraction ----------
    candidate_skills: Set[str] = set(extract_skills(resume_text, role=role))
    required_skills: Set[str] = ROLE_SKILLS[role]

    # ---------- Comparison ----------
    matched_skills = candidate_skills & required_skills
    missing_skills = required_skills - candidate_skills
    extra_skills = candidate_skills - required_skills

    # ---------- Scoring ----------
    total_required = len(required_skills)
    match_percentage = (
        round((len(matched_skills) / total_required) * 100, 2)
        if total_required > 0 else 0.0
    )

    # ---------- Priority Classification ----------
    priority_breakdown = {
        "critical": [],
        "high": [],
        "medium": [],
        "low": []
    }

    for skill in missing_skills:
        priority = SKILL_PRIORITY.get(skill, "low")
        priority_breakdown[priority].append(skill)

    # ---------- Recommendations ----------
    recommendations = _generate_recommendations(
        priority_breakdown["critical"],
        priority_breakdown["high"],
        role
    )

    # ---------- Result ----------
    result: Dict[str, Any] = {
        "role": role,
        "match_percentage": match_percentage,
        "rating": _get_rating(match_percentage),

        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills),
        "extra_skills": sorted(extra_skills),

        "total_required": total_required,
        "total_matched": len(matched_skills),
        "total_missing": len(missing_skills),

        "priority_breakdown": {
            k: sorted(v) for k, v in priority_breakdown.items()
        },

        "recommendations": recommendations
    }

    # ---------- Learning Resources ----------
    if include_resources:
        result["learning_resources"] = {
            skill: LEARNING_RESOURCES[skill]
            for skill in missing_skills
            if skill in LEARNING_RESOURCES
        }

    return result

# ==================================================
# HELPERS
# ==================================================

def _get_rating(percentage: float) -> str:
    """Convert percentage to human-readable rating."""
    if percentage >= 90:
        return "Excellent ⭐⭐⭐⭐⭐"
    if percentage >= 75:
        return "Strong ⭐⭐⭐⭐"
    if percentage >= 60:
        return "Good ⭐⭐⭐"
    if percentage >= 40:
        return "Fair ⭐⭐"
    return "Needs Improvement ⭐"


def _generate_recommendations(
    critical: List[str],
    high: List[str],
    role: str
) -> List[str]:
    """Generate actionable recommendations."""
    recs: List[str] = []

    if critical:
        recs.append(
            f"🚨 PRIORITY: Learn critical skills first: {', '.join(critical)}"
        )

    if high:
        recs.append(
            f"📌 IMPORTANT: Add high-impact skills: {', '.join(high[:3])}"
        )

    if not critical and not high:
        recs.append(
            f"✅ You meet all critical requirements for the {role} role."
        )

    return recs

# ==================================================
# ROLE COMPARISON
# ==================================================

def compare_multiple_roles(resume_text: str) -> Dict[str, Any]:
    """
    Compare resume against all roles and rank them.
    """

    results = []
    for role in ROLE_SKILLS:
        analysis = analyze_skill_gap(resume_text, role)
        results.append({
            "role": role,
            "match_percentage": analysis["match_percentage"]
        })

    results.sort(key=lambda x: x["match_percentage"], reverse=True)

    return {
        "best_match": results[0],
        "all_matches": results
    }

# ==================================================
# ROADMAP GENERATOR
# ==================================================

def get_skill_roadmap(role: str) -> Dict[str, Any]:
    """
    Generate a learning roadmap for a role.
    """

    if role not in ROLE_SKILLS:
        raise ValueError("Invalid role")

    roadmap = {
        "fundamentals": [],
        "intermediate": [],
        "advanced": []
    }

    for skill in ROLE_SKILLS[role]:
        priority = SKILL_PRIORITY.get(skill, "low")
        if priority == "critical":
            roadmap["fundamentals"].append(skill)
        elif priority == "high":
            roadmap["intermediate"].append(skill)
        else:
            roadmap["advanced"].append(skill)

    return {
        "role": role,
        "roadmap": roadmap
    }

# ==================================================
# DEV TEST
# ==================================================

if __name__ == "__main__":
    sample_resume = """
   alex rivera 123 tech lane, san francisco, ca 94105 (555) 012-3456 | alex.rivera.dev@email.com linkedin.com/in/alexrivera | github.com/arivera-codes professional summary dynamic and detail-oriented software engineer with over 5 years of experience in full-stack development. proven track record of optimizing system performance and leading cross-functional teams to deliver scalable web applications. passionate about ai integration and cloud-native architecture. work experience senior software engineer | techflow solutions january 2021 – present • led the migration of a legacy monolithic architecture to a microservices-based system using node.js and docker, reducing deployment time by 40%. • developed and maintained restful apis for a high-traffic e-commerce platform serving over 500k monthly active users. • mentored 4 junior developers and conducted weekly code reviews to ensure high-quality standards. junior web developer | innovate web lab june 2018 – december 2020 • collaborated with ui/ux designers to implement responsive front-end components using react.js and tailwind css. • identified and resolved 50+ critical bugs in the database layer, improving application stability by 15%. • integrated third-party payment gateways (stripe, paypal) ensuring secure transaction processing. education bachelor of science in computer science state university of technology | 2014 – 2018 • gpa: 3.8/4.0 • relevant coursework: data structures, algorithms, database management, software engineering. technical skills • languages: javascript (es6+), python, java, sql, html5, css3. • frameworks/libraries: react, node.js, express, django, redux. • tools & platforms: git, aws (ec2, s3), docker, jenkins, postgresql, mongodb. • soft skills: agile methodology, problem solving, technical documentation, team leadership. projects ai-powered task manager • built a task management tool using python and openai api to automatically prioritize user tasks based on deadlines and sentiment analysis. • deployed the application on heroku with a ci/cd pipeline.
    """

    result = analyze_skill_gap(sample_resume, "backend", include_resources=True)
    print(result)



