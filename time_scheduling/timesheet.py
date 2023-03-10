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

class TimeSheet:
    def __init__(s, time_sheet_file):
        s.time_sheet_file = time_sheet_file

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