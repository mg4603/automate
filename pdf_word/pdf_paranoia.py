from pathlib import Path
from sys import exit
from argparse import ArgumentParser
try:
    from PyPDF2 import PdfFileReader, PdfFileWriter
except ImportError:
    exit('This program requires PyPDF2 to run.')

def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        'dir_path', metavar='dir-path', 
        help='Directory path to files to encrypt or decrypt'
    )
    parser.add_argument(
        '-e', '--encrypt', action='store_true', 
        help='Encrypt or Decrypt'
    )
    return parser.parse_args()

def get_password(filename):
    print('Enter password for {}:'.format(filename))
    password = input('> ')
    return password

def main():
    args = parse_args()
    print('Pdf Paranoia')
    print()

    password = get_password()
    if args.encrypt:
        print('Encrypting...')
        encrypt(args.dir_path)
    else:
        print('Decrypting...')
        decrypt(args.dir_path)

    print('Done')

if __name__ == '__main__':
    main()