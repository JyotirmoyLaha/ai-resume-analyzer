from flask import Flask, request, jsonify
from flask_cors import CORS

from resume_parser import extract_text_from_resume
from skill_gap import (
    analyze_skill_gap,
    compare_multiple_roles,
    get_skill_roadmap,
    get_available_roles
)

app = Flask(__name__)
CORS(app)

# ============================
# HEALTH CHECK
# ============================
@app.route("/", methods=["GET"])
def health():
    return jsonify({
        "status": "OK",
        "message": "AI Resume Analyzer API is running"
    })


# ============================
# ANALYZE RESUME
# ============================
@app.route("/analyze", methods=["POST"])
def analyze_resume():

    # ✅ File validation
    if "resume" not in request.files:
        return jsonify({"error": "Resume file is required"}), 400

    resume_file = request.files.get("resume")

    if resume_file.filename == "":
        return jsonify({"error": "Resume file is empty"}), 400

    role = request.form.get("role", "").lower().strip()
    include_resources = request.form.get("include_resources", "false").lower() == "true"

    try:
        resume_text = extract_text_from_resume(resume_file)

        if not resume_text:
            return jsonify({"error": "Unable to extract text from resume"}), 400

        result = analyze_skill_gap(
            resume_text=resume_text,
            role=role,
            include_resources=include_resources
        )

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ============================
# AVAILABLE ROLES
# ============================
@app.route("/roles", methods=["GET"])
def roles():
    return jsonify(get_available_roles())


# ============================
# RUN APP
# ============================
if __name__ == "__main__":
    app.run()

