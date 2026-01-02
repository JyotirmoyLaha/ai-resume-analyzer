# resume_parser.py

import pdfplumber
import re

def extract_text_from_resume(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    # Basic cleaning
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()

    return text


# TESTING
if __name__ == "__main__":
    resume_text = extract_text_from_resume("sample_resume.pdf")
    print(resume_text[:10000])  # print first 10000 chars
