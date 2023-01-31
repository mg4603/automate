from argparse import ArgumentParser
from pathlib import Path
from sys import exit
try:
    from docx import Document
except ImportError:
    exit('This program requires the python-docx module to run.')

def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        'wordlist', help='wordlist of passwords to bruteforce'
    )
    parser.add_argument(
        'pdf', help='encrypted pdf to bruteforce password of'
    )
    return parser.parse_args()

if __name__ == '__main__':
    main()