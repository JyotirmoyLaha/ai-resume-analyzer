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
    "postgresql": "https://www.postgresql.org/docs/current/tutorial.html",
    "flask": "https://flask.palletsprojects.com/en/2.3.x/tutorial/",
    "nextjs": "https://nextjs.org/learn",
    "kubernetes": "https://kubernetes.io/docs/tutorials/",
    "machine_learning": "https://www.coursera.org/learn/machine-learning",
    "deep_learning": "https://www.deeplearning.ai/deep-learning-specialization/",
    "nlp": "https://www.coursera.org/learn/natural-language-processing",
    "git": "https://git-scm.com/docs/gittutorial",
    "typescript": "https://www.typescriptlang.org/docs/",
    "ci_cd": "https://www.redhat.com/en/topics/devops/what-is-ci-cd",
    "tailwind": "https://tailwindcss.com/docs/installation",
}

# ==================================================
# PRIORITY WEIGHTING (FOR REALISTIC SCORING)
# ==================================================

def _priority_weight(priority: str) -> int:
    return {
        "critical": 3,
        "high": 2,
        "medium": 1,
        "low": 0
    }.get(priority, 0)

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
    candidate_skills: Set[str] = set(extract_skills(resume_text))
    required_skills: Set[str] = ROLE_SKILLS[role]

    # ---------- Comparison ----------
    matched_skills = candidate_skills & required_skills
    missing_skills = required_skills - candidate_skills
    extra_skills = candidate_skills - required_skills

    # ---------- Weighted Scoring ----------
    total_score = 0
    earned_score = 0

    for skill in required_skills:
        weight = _priority_weight(SKILL_PRIORITY.get(skill, "low"))
        total_score += weight
        if skill in candidate_skills:
            earned_score += weight

    match_percentage = (
        round((earned_score / total_score) * 100, 2)
        if total_score > 0 else 0.0
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

        "total_required": len(required_skills),
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
    result["career_feedback"] = generate_career_feedback(result)

    return result


# ==================================================
# Feedback Generator
# ==================================================
def generate_career_feedback(result: Dict[str, Any]) -> str:
    role = result["role"]
    match = result["match_percentage"]
    critical = result["priority_breakdown"]["critical"]
    high = result["priority_breakdown"]["high"]
    medium = result["priority_breakdown"]["medium"]

    if match >= 85:
        feedback = (
            f"You are strongly prepared for the {role} role. "
            "Your core skills align well with industry expectations."
        )
    elif match >= 65:
        feedback = (
            f"You are moderately prepared for the {role} role, "
            "but strengthening a few areas will significantly improve your chances."
        )
    else:
        feedback = (
            f"You are currently underprepared for the {role} role. "
            "Focused upskilling is recommended before applying."
        )

    if critical:
        feedback += (
            f" Critical gaps detected in {', '.join(critical)}. "
            "These should be your top priority."
        )

    if high:
        feedback += (
            f" Adding {', '.join(high[:2])} will greatly strengthen your profile."
        )

    if not critical and not high:
        feedback += " You meet all major expectations for this role."

    return feedback

# ==================================================
# HELPERS
# ==================================================

def get_available_roles() -> List[str]:
    """
    Return all supported job roles.
    """
    return sorted(ROLE_SKILLS.keys())

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
            f"🚨 Focus immediately on core {role} skills: {', '.join(critical)}"
        )

    if high:
        recs.append(
            f"📈 Strengthen your profile by adding: {', '.join(high)}"
        )

    if not critical and not high:
        recs.append(
            f"✅ Your resume strongly matches the {role} role requirements."
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

    role = role.lower().strip()
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

