from argparse import ArgumentParser
from sys import exit
from pathlib import Path
try:
    from openpyxl import load_workbook
except ImportError:
    exit('This program requires the openpyxl module to run.')

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('file', help='file to invert cells of')
    return parser.parse_args()

if __name__ == '__main__':
    main()