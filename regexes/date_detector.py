'''
1) Copy date from clipboard
2) create regex to detect date in dd/mm/yyyy format
3) add function to validate if date exists
4) paste valid dates to clipboard
'''
try:
    from pyperclip import copy, paste
except ImportError:
    exit('This program requires pyperclip.')

def main():
    text = paste()

    dates = date_regex.findall(text)
    valid_dates = get_valid_dates(dates)
    formatted_str = get_formatted_dt_str(valid_dates)


    print(formatted_str)
    copy(formatted_str)
    print('(Copied to clipboard.')



if __name__ == '__main__':
    main()