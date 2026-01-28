import PyPDF2

def parse_resume(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()

    keywords = ["python", "django", "sql", "ml", "api", "data"]
    skills = [k for k in keywords if k.lower() in text.lower()]
    return skills
