from pathlib import Path
from sys import exit
from logging import debug, DEBUG, CRITICAL, disable, basicConfig
try:
    from openpyxl import Workbook
    from openpyxl.styles import Font
except ImportError:
    exit('This program requires teh openpyxl module to run.')

basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# disable(CRITICAL)

def main():
    print('Multiplication Table xlsx')
    print()
    print('Opening workbook...')

    wb = Workbook()
    debug(wb)
    debug(wb.sheetnames)
    sheet = wb['Sheet']

    font_obj = Font(bold=True)
    for i in range(1,7):
        sheet.cell(row=1, column=i + 1).value = i
        sheet.cell(row=1, column=i + 1).font = font_obj
        debug(sheet.cell(row=1, column=i+1).value)
    
    for i in range(1, 7):
        sheet.cell(row=i + 1, column=1).value = i
        sheet.cell(row=i + 1, column=1).font = font_obj
        debug(sheet.cell(row=i + 1, column=1).value)
    
    for i in range(1, 7):
        for j in range(1, 7):
            sheet.cell(row=i + 1, column=j + 1).value = i * j
            debug(
                '({}, {}): {}'.format(
                    i + 1,
                    j + 1,
                    sheet.cell(row=i + 1, column=j + 1).value
                )
            )
    
    wb.save('multiplication_table.xlsx')

