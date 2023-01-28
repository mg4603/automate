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




if __name__ == '__main__':
    main()