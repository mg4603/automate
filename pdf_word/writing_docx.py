from sys import exit
try:
    from docx import Document
except ImportError:
    exit('This program requires python-docx to run.')


def hello_world():
    doc = Document()
    doc.add_paragraph('Hello, world!')
    doc.save('hello_world.docx')



# hello_world()