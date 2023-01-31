from argparse import ArgumentParser
from pathlib import Path
from logging import debug, disable, basicConfig, DEBUG, CRITICAL
from sys import exit
try:
    from PyPDF2 import PdfFileReader
except ImportError:
    exit('This program requires PyPDF2 module to run.')
basicConfig(
    level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s'
)
# disable(CRITICAL)

def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        'wordlist', help='wordlist of passwords to bruteforce'
    )
    parser.add_argument(
        'pdf', help='encrypted pdf to bruteforce password of'
    )
    return parser.parse_args()

def main():
    print('PDF Bruteforcer')
    print()
    args = parse_args()
    with Path(args.wordlist).open('r') as file:
        lines = [line.strip().lower() for line in  file.readlines()]
        for word in lines:
            # debug(word)
            pdf_reader = PdfFileReader(Path(args.pdf).open('rb'))
            if pdf_reader.decrypt(word):
                print(word)
                exit('Done')
            elif pdf_reader.decrypt(word.upper()):
                print(word.upper())
                exit('Done')
    
    print('Password not found.')

if __name__ == '__main__':
    main()