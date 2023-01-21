'''
1) copy from clipboard
2) extract phone nums and emails
3) format them 
4) paste to clipboard
'''
from re import compile, VERBOSE
from sys import exit
try:
    from pyperclip import copy, paste
except ImportError:
    exit('This program requires pyperclip')

phone_regex = compile(
    r'''
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    '''
    ,VERBOSE
)

def main():
    text = paste()

    phone_numbers = phone_regex.findall(text)
    emails = email_regex.findall(text)

    if len(phone_numbers) == 0 and len(emails) == 0:


    formatted_string = get_formatted_output(phone_numbers, emails)
    print('Formatted output:')
    print(formatted_string)
    
    copy(formatted_string)
    print('(Copied to clipboard.)')

if __name__ == '__main__':
    main()