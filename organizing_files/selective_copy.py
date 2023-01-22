'''
1) get src path
2) get dest path
3) get ext of files to copy
4) do the copying
'''
from pathlib import Path
from re import escape, compile

def get_src_path():
    print('Enter src path dir to copy files from:')
    while True:
        src_name = input('> ')
        src_path = Path(src_name)
        if src_path.exists():
            if src_path.is_dir():
                return src_path
            print('Source path isn\'t a directory')
        else:
            print('Source path doesn\'t exist.')

def main():
    print('Selective Copy')
    print()
    src_path = get_src_path()

    print('Enter destination name:')
    dest_name = input('>')

    dest_path = Path(dest_name)
    dest_path.mkdir(parents=True, exist_ok=True)

    print('Enter extension of files to copy:')
    ext = input('> ')
    ext_reg = compile(escape(ext))

    copy_files(src_path, dest_path, ext_reg)
    print('Copying Done.')

if __name__ == '__main__':
    main()