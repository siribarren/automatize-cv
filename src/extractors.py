# src/extractors.py
import pdfplumber
from docx import Document

def extraer_texto_pdf(pdf_file):
    texto = ""
    with pdfplumber.open(pdf_file) as pdf:
        for pagina in pdf.pages:
            texto += pagina.extract_text() + "\n"
    return texto.strip()

def extraer_texto_word(word_file):
    doc = Document(word_file)
    texto = "\n".join([p.text for p in doc.paragraphs])
    return texto.strip()
