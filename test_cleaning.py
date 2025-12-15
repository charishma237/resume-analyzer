from utils.resume_parser import extract_text_from_pdf
from utils.text_cleaning import clean_text

raw_text = extract_text_from_pdf("resume.pdf")
cleaned_text = clean_text(raw_text)

print("RAW TEXT:\n", raw_text[:500])
print("\nCLEANED TEXT:\n", cleaned_text[:500])
