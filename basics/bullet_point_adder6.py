from sys import exit
try:
    from pyperclip import copy, paste
except ImportError:
    exit('This script requires pyperclip.')

def main():
    text = paste()
    new_text = ''
    for line in text.split('\n'):
        new_text += '* ' + line + '\n'
    print(new_text)
    copy(new_text)

if __name__ == '__main__':
    main()