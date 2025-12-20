from flask import Flask, render_template, request
from utils.resume_parser import extract_text_from_pdf
from utils.text_cleaning import clean_text
from utils.skill_extracter import extract_skills
from utils.similarity import calculate_similarity

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.files["resume"]
    job_desc = request.form["job"]

    resume_text = extract_text_from_pdf(resume)
    resume_clean = clean_text(resume_text)
    skills = extract_skills(resume_clean)

    job_clean = clean_text(job_desc)
    score = calculate_similarity(resume_clean, job_clean)

    return render_template(
        "result.html",
        skills=skills,
        score=round(score * 100, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)
