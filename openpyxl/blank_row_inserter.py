from pathlib import Path
from argparse import ArgumentParser
from logging import debug, DEBUG, CRITICAL, disable, basicConfig
try:
    from openpyxl import load_workbook
except ImportError:
    exit('This program requires the openpyxl module to run.')

basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
disable(CRITICAL)

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('N', help='row to start insertions after')
    parser.add_argument('M', help='number of blank rows to insert')
    parser.add_argument('file', help='file to perform insertions on')
    return parser.parse_args()

def main():
    print('Blank row inserter')
    print()
    args = parse_args()

    print('Opening workbook...')
    workbook_path = Path(args.file)
    if not workbook_path.exists():
        exit('Selected file doesn\'t exist.')
    
    workbook = load_workbook(workbook_path)
    sheet = workbook[workbook.sheetnames[0]]
    debug(sheet.title)

    try:
        N = int(args.N)
        M = int(args.M)
    except TypeError:
        exit('M and N should be integers.')

    sheet.insert_rows(N, amount=M)

    new_workbook_path = Path('blank_rows_' + args.file)
    workbook.save(new_workbook_path)
    print('Done')
    
    


if __name__ == '__main__':
    main()