'''
1) accept a string input
2) remove second argument from first arg
3) if second argument doesn't exist remove whitespaces at start and end
'''

def main():
    print('STRIP')
    print()
    print('Enter char to strip:')
    char = input('> ')
    print('Enter string to strip from:')
    string = input('> ')
    if char == '':
        stripped_string = strip(string)
    else:
        stripped_string = strip(string, char)
    print()
    print('Stripped string:')
    print(stripped_string)

if __name__ == '__main__':
    main()