#! /usr/bin/env python3
# tabulate population and number of census tracts for each county
'''
1) read with openpyxl
2) count census tracts in each county
3) count population of each county
4) prints results
'''
from sys import exit
from logging import debug, DEBUG, CRITICAL, disable, basicConfig
from pathlib import Path
from pprint import pformat
try:
    from openpyxl import load_workbook
except ImportError:
    exit('This program requires the openpyxl module to run.')

basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# disable(CRITICAL)

def main():
    print('Read and Tabulate census 2010 data')
    print()
    print('Opening workbook...')
    wb = load_workbook('censuspopdata.xlsx')
    pop_sheet = wb[wb.sheetnames[0]]

    debug(pop_sheet.title)

    county_data = {}

    for i in range(2, pop_sheet.max_row + 1):
        state = pop_sheet.cell(row=i, column=2).value
        county = pop_sheet.cell(row=i, column=3).value
        population = pop_sheet.cell(row=i, column=4).value
        if state not in county_data:
            county_data[state] = {}
        
        if county not in county_data[state]:
            county_data[state][county] = {'population': 0, 'tracks': 0}
        
        county_data[state][county]['population'] += population
        county_data[state][county]['tracks'] += 1
    
    with Path('census2010.py').open('w') as file:
        debug('all_data ='+ pformat(county_data))
        file.write('all_data ='+ pformat(county_data))

if __name__ == '__main__':
    main()