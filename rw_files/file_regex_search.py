'''
1) get all txt files in dir
2) get regex from user
3) check all files for regex
4) prints results to screen
'''
from pathlib import Path
from re import escape, compile

def main():
    print('Interactive Grep')
    print()
    directory = get_directory()
    
    print('Enter regex to search for:')
    regex_string = input('> ')
    regex_string = escape(regex_string)
    regex = compile(regex_string)

    for file in directory.glob('*.txt'):
        with file.open('r') as f:
            for line in f.readlines():
                if regex.search(line):
                    print('{}: {}'.format(
                        file.name, line
                    ))
                

if __name__ == '__main__':
    main()