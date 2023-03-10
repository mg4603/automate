"""
1. take a name as input
2. check csv file for name
3. if it exists:
    1. if both check-in and check-out are filled keep looking
    2. if only check in if filled in fill checkout
    3. if non filled entry doesn't exist create new entry with 
       check in time
"""
from sys import exit
from pathlib import Path
from csv import reader, writer
from time import time
from logging import debug, disable, basicConfig, DEBUG, CRITICAL
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s ')
disable(CRITICAL)

class TimeSheet:
    def __init__(s, time_sheet_file):
        s.time_sheet_file = Path(time_sheet_file)
        if not s.time_sheet_file.exists():
            debug(1)
            s.time_sheet_file.open('w')
    
    def record(s, name):
        time_sheet = []
        with s.time_sheet_file.open('r') as file:
            csv_reader = reader(file)
            new_entry = True
            for row in csv_reader:
                if row[0] == name:
                    debug(row)
                    debug(row[0] == name)
                    if not len(row) == 3:
                        debug(len(row))
                        new_entry = False
                        time_sheet.append([row[0], row[1], time()])
                    else:
                        time_sheet.append(row)
                else:
                    time_sheet.append(row)
            if new_entry:
                time_sheet.append([name, time()])

        with s.time_sheet_file.open('w') as file:
            csv_writer = writer(file)
            for row in time_sheet:
                csv_writer.writerow(row)

def main():
    print('------------------------Time Sheet-----------------')
    time_sheet = TimeSheet('timesheet.csv')
    try:
        while True:
            print('Enter Name:')
            name = input('> ')
            time_sheet.record(name)
            
    except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    main()