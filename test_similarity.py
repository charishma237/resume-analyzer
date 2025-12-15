from utils.text_cleaning import clean_text
from utils.similarity import calculate_similarity

resume_text = clean_text("python developer with machine learning experience")
job_text = clean_text("looking for machine learning engineer skilled in python")

score = calculate_similarity(resume_text, job_text)
print("Match Score:", round(score * 100, 2), "%")
