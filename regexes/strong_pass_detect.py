'''
requirements:
1) 8 chars long
2) has atleast one digit
3) contains both uppercase and lower case characters

steps:
1) take password as input
2) check if requirements are met
3) return true or false accordingly

'''
from re import compile

length_regex = compile(r'\w{8,}')
digit_regex = compile(r'\d')
upper_regex = compile(r'[A-Z]')
lower_regex = compile('r[a-z]')

def is_strong(password, regexes):
    for regex in regexes:
        if regex.search(password) == None:
            return False
    return True

def main():
    regexes = [length_regex, digit_regex, upper_regex, lower_regex]
    print('Strong Password')
    print()
    print('Requirements:')
    print('\t1) 8 chars long')
    print('\t2) Has at least one digit')
    print('\t3) contains both upper and lower case characters')
    print()
    print('Enter password to check:')

    password = input('> ')
    if is_strong(password, regexes):
        print('The password matches the required strength conditions.')
    else:
        print('The password doesn\'t match the required strength conditions.')

if __name__ == '__main__':
    main()