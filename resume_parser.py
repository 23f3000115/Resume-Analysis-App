import pdfplumber
from PyPDF2 import PdfReader

def extract_text_from_pdf(path):
    text = ''
    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text() or ''
                text += page_text + '\n'
    except Exception:
        try:
            reader = PdfReader(path)
            for p in reader.pages:
                page_text = p.extract_text() or ''
                text += page_text + '\n'
        except Exception as e:
            text = ''
    return text.strip()
