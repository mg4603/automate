#! /usr/bin/env python3
# tabulate population and number of census tracts for each county
'''
1) read with openpyxl
2) count census tracts in each county
3) count population of each county
4) prints results
'''
from sys import exit
try:
    from openpyxl import load_workbook
except ImportError:
    exit('This program requires the openpyxl module to run.')

if __name__ == '__main__':
    main()