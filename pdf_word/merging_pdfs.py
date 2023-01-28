from sys import exit
from pathlib import Path
from logging import debug, DEBUG, CRITICAL, disable, basicConfig
from argparse import ArgumentParser
try:
    from PyPDF2 import PdfFileReader, PdfFileWriter
except ImportError:
    exit('This program requires PyPDF2 to run.')

basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# disable(CRITICAL)

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

    first_file = pdf_files[0].open('rb')
    first_page = PdfFileReader(first_file).getPage(0)
    debug(first_page.extractText())
    pdf_writer.addPage(first_page)
    first_file.close()

    debug(pdf_writer.getNumPages())

    for file in pdf_files:
        file_obj = file.open('rb')

        pdf_reader = PdfFileReader(file_obj)
        if pdf_reader.isEncrypted:
            continue

        for page_num in range(1, pdf_reader.numPages):
            page_obj = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page_obj)    
            
    debug(pdf_writer.getNumPages())

    result_file = dir_path / 'merged_pdfs.pdf'
    file_obj = result_file.open('wb')
    pdf_writer.write(file_obj)
    file_obj.close()

    print('Done')

if __name__ == '__main__':
    main()