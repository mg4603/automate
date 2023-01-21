'''
1) Copy date from clipboard
2) create regex to detect date in dd/mm/yyyy format
3) add function to validate if date exists
4) paste valid dates to clipboard
'''
from re import compile, VERBOSE
try:
    from pyperclip import copy, paste
except ImportError:
    exit('This program requires pyperclip.')

date_regex = compile(
    r'''
    ([0-2][1-9]|3[01])
    (\s|-|/)
    (0[1-9]|1[0-2])
    (\s|-|/)
    ([12][0-9]{3})
    ''',
    VERBOSE
)

def get_valid_dates(dates):
    valid_dates = []
    for date in dates:
        day, _, month, _, year = date
        if month in (
                '01', '03', '05', '07', '08', '10', '12'
                ):
            if 0 < int(day) <= 31:
                valid_dates.append(date)
        elif month in (
                '04', '06', '09', '11'
                ):
            if 0 < int(day) <= 30:
                valid_dates.append(date)
        else:
            year = int(year)
            if year % 400 == 0:
                if 0 < int(day) <= 29:
                    valid_dates.append(date)
            elif year % 4 == 0 and not year % 100 == 0:
                if 0 < int(day) <= 29:
                    valid_dates.append(date)
            else:
                if 0 < int(day) <= 28:
                    valid_dates.append(date)
    return valid_dates

def main():
    text = paste()

    dates = date_regex.findall(text)
    valid_dates = get_valid_dates(dates)
    print(valid_dates)
    formatted_str = get_formatted_dt_str(valid_dates)


    print(formatted_str)
    copy(formatted_str)
    print('(Copied to clipboard.')



if __name__ == '__main__':
    main()