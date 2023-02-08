'''
1) take path as cmd line arg
2) get all xlsx files in the dir
3) transform all spread sheets into csv files - one per sheet
4) name csv files <file_name>_<sheet_name>.csv
'''
from argparse import ArgumentParser
from sys import exit
try:
    from openpyxl import load_workbook
except ImportError:
    exit('This program requires the openpyxl module to run.')

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('dir', help='path to dir of xlsx files to convert')
    return parser.parse_args()



if __name__ == '__main__':
    main()