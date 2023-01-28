from sys import exit
from pathlib import Path
from logging import debug, DEBUG, CRITICAL, disable, basicConfig
from argparse import ArgumentParser
try:
    from PyPDF2 import PdfFileReader, PdfFileWriter
except ImportError:
    exit('This program requires PyPDF2 to run.')

basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
disable(CRITICAL)

def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        'dir_path', metavar='dir-path', help='path to directory with files to merge'
    )
    return parser.parse_args()

def main():
    args = parse_args()
    debug(args)

    print('Merging PDFs')
    print()
    dir_path = Path(args.dir_path).absolute()
    if not dir_path.exists():
        exit('The directory {} doesn\'t exist.'.format(dir_path.name))
    
    pdf_writer = PdfFileWriter()
    pdf_files = list(dir_path.glob('*.pdf'))
    pdf_files.sort()

    with open(pdf_files[0], 'rb') as first_file:
        first_page = PdfFileReader(first_file).getPage(0)
        pdf_writer.addPage(first_page)

    debug(pdf_writer.getNumPages())
    for file in pdf_files:
        with file.open('rb') as file_obj:
            pdf_reader = PdfFileReader(file_obj)
            if pdf_reader.isEncrypted:
                continue
            for page_num in range(1, pdf_reader.numPages):
                pdf_writer.addPage(pdf_reader.getPage(page_num))
    
    debug(pdf_writer.getNumPages())

    result_file = dir_path / 'merged_pdfs.pdf'
    with result_file.open('wb') as file_obj:
        pdf_writer.write(file_obj)

    print('Done')

if __name__ == '__main__':
    main()