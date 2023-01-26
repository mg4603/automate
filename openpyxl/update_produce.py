from logging import debug, DEBUG, CRITICAL, disable, basicConfig
from pathlib import Path
from sys import exit
try:
    from openpyxl import load_workbook
except ImportError:
    exit('This program requires openpyxl to run.')

basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
disable(CRITICAL)

def main():
    print('Update Produce Spreadsheet')
    print()
    print('Opening workbook...')
    wb = load_workbook('produce_sales.xlsx')

    produce_sheet = wb[wb.sheetnames[0]]
    debug(wb.sheetnames)
    debug(produce_sheet)

    updated_prices = {
        'Celery': 1.19,
        'Garlic': 3.07,
        'Lemon': 1.27
    }

    for i in range(2, produce_sheet.max_row + 1):
        produce_name = produce_sheet.cell(row=i, column=1).value
        if produce_name in updated_prices:
            debug('produce name: ' + produce_name)
            debug(
                '{}{}'.format('produce price:', 
                produce_sheet.cell(row=i, column=2).value)
            )
            debug(
                '{}{}'.format('updated price: ',
                updated_prices[produce_name])
            )
            produce_sheet.cell(row=i, column=2).value = \
                updated_prices[produce_name]
    
    wb.save('updated_produce_sales.xlsx')

if __name__ == '__main__':
    main()