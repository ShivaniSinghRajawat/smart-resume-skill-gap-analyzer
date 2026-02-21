import os
from PyPDF2 import PdfReader
from docx import Document

def parse_pdf(file_path):
    """
    Parse a PDF file and extract text.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    text = ""
    with open(file_path, 'rb') as file:
        pdf = PdfReader(file)
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def parse_docx(file_path):
    """
    Parse a DOCX file and extract text.

    Args:
        file_path (str): The path to the DOCX file.

    Returns:
        str: Extracted text from the DOCX.
    """
    text = ""
    doc = Document(file_path)
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text.strip()

def parse_txt(file_path):
    """
    Parse a TXT file and extract text.

    Args:
        file_path (str): The path to the TXT file.

    Returns:
        str: Extracted text from the TXT.
    """
    with open(file_path, 'r') as file:
        return file.read().strip()

def parse_resume(file_path):
    """
    Parse a resume from a PDF, DOCX, or TXT file.

    Args:
        file_path (str): The path to the resume file.

    Returns:
        str: Extracted text from the resume based on its file type.
        
    Raises:
        ValueError: If the file type is unsupported.
    """
    if not os.path.exists(file_path):
        raise ValueError("The file does not exist.")
    
    extension = os.path.splitext(file_path)[-1].lower()
    if extension == '.pdf':
        return parse_pdf(file_path)
    elif extension == '.docx':
        return parse_docx(file_path)
    elif extension == '.txt':
        return parse_txt(file_path)
    else:
        raise ValueError("Unsupported file type: {}".format(extension))
