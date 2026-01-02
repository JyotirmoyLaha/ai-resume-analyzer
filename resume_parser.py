import pdfplumber
import re
from typing import Optional
from werkzeug.datastructures import FileStorage


def extract_text_from_resume(file: FileStorage) -> Optional[str]:
    """
    Extract and clean text from uploaded PDF resume
    """

    if not file or not hasattr(file, "filename"):
        return None

    extracted_text = []

    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    extracted_text.append(text)

    except Exception as e:
        print(f"[ERROR] PDF parsing failed: {e}")
        return None

    if not extracted_text:
        return None

    text = "\n".join(extracted_text)

    # Clean text
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n+", "\n", text)

    return text.lower().strip()
