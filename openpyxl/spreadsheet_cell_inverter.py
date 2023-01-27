from argparse import ArgumentParser
from sys import exit
from pathlib import Path
from logging import debug, DEBUG, CRITICAL, disable, basicConfig
try:
    from openpyxl import load_workbook, Workbook
except ImportError:
    exit('This program requires the openpyxl module to run.')

basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# disable(CRITICAL)

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('file', help='file to invert cells of')
    return parser.parse_args()

def main():
    print('Spreadsheet Cell Inverter')
    print()
    print('Opening Workbook...')

    args = parse_args()

    workbook_path = Path(args.file)
    wb = load_workbook(workbook_path)
    sheet = wb[wb.sheetnames[0]]

    new_wb = Workbook()
    new_wb_sheet = new_wb[new_wb.sheetnames[0]]
    new_wb_sheet.title = sheet.title

    print('Starting inversion...')
    for i in range(1, sheet.max_row + 1):
        for j in range(1, sheet.max_column + 1):
            debug(sheet.cell(row=i, column=j).value)
            new_wb_sheet.cell(row=j, column=i).value = \
                sheet.cell(row=i, column=j).value
    
    print('Saving to file')
    new_wb.save('inverted_'+args.file)
    print('Done')



if __name__ == '__main__':
    main()