from utils.resume_parser import extract_text_from_pdf
from utils.text_cleaning import clean_text
from utils.skill_extracter import extract_skills

raw = extract_text_from_pdf("resume.pdf")
cleaned = clean_text(raw)

skills = extract_skills(cleaned)
print("Extracted Skills:", skills)
