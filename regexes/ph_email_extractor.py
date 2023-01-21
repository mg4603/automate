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
email_regex = compile(
    r'''
    ([a-zA-Z0-9._-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4}))
    ''',
    VERBOSE
)

def get_formatted_out(phone_numbers, emails):
    formatted_str = ''
    
    if len(phone_numbers):
        for i, ph_num in enumerate(phone_numbers):
            if ph_num[0]:
                phone_numbers[i] = '-'.join([ph_num[0], ph_num[2], ph_num[4]])
            else:
                phone_numbers[i] = '-'.join([ph_num[2], ph_num[4]])

            if ph_num[7] != '':
                phone_numbers[i] += ' x' + ph_num[7]
    
        formatted_str += 'Phone Numbers:\n\t'
        formatted_str += '\n\t'.join(phone_numbers)
    
    if len(emails):
        for i, email in enumerate(emails):
            emails[i] = email[0]
    
        formatted_str += '\nEmails:\n\t'
        formatted_str += '\n\t'.join(emails)

    return formatted_str

def main():
    text = paste()

    phone_numbers = phone_regex.findall(text)
    emails = email_regex.findall(text)

    if len(phone_numbers) == 0 and len(emails) == 0:
        print('No phone number or emails found.')
        exit()

    formatted_string = get_formatted_out(phone_numbers, emails)
    print('Formatted output:')
    print(formatted_string)
    
    copy(formatted_string)
    print('(Copied to clipboard.)')

if __name__ == '__main__':
    main()