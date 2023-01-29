#! python3

from sys import exit
try:
    from docx import Document
except ImportError:
    exit('This module requires the python-docx module to run.')

def get_text(filename):
    doc = Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    
    return '\n'.join(full_text)