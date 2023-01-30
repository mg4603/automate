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

def encrypt(directory_name):
    dir_path = Path(directory_name).absolute()
    encrypted_dir = dir_path / 'encrypted'
    encrypted_dir.mkdir(parents=True, exist_ok=True)
    for file in dir_path.glob('*.pdf'):
        pdf_reader = PdfFileReader(file.open('rb'))
        if pdf_reader.isEncrypted:
            continue
        pdf_writer = PdfFileWriter()
        for page_num in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))
        
        password = get_password(file.name)
        pdf_writer.encrypt(password)
        pdf_writer.write(
            (encrypted_dir / (file.stem + '_encrypted.pdf')).open('wb')
        )


def main():
    args = parse_args()
    print('Pdf Paranoia')
    print()

    if args.encrypt:
        print('Encrypting...')
        encrypt(args.dir_path)
    else:
        print('Decrypting...')
        decrypt(args.dir_path)

    print('Done')

if __name__ == '__main__':
    main()