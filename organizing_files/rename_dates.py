'''
1) get files in user defined dir
2) Id files with names in european date style
3) rename files to american date style
'''
from re import compile, VERBOSE
from pathlib import Path
from shutil import move
from os.path import join

american_date_regex = compile(
    r'''
    (0[1-9]|1[0-2])
    -
    (0[1-9]|12[0-9]|3[0-1])
    -
    ([12]\d{3})
    (.*?)$
    ''',
    VERBOSE
)
def get_dir_path():
    print('Enter path of dir with files to rename:')
    while True:
        dir_name = input('> ')
        if Path(dir_name).is_dir():
            return Path(dir_name)
        print('Directory doesn\'t exist')

def rename_files(dir_path, american_date_regex):
    for file in dir_path.glob('*'):
        mo = american_date_regex.search(str(file.name))
        if mo:
            new_name = '-'.join([mo.group(2), mo.group(1), mo.group(3)]) + mo.group(4)
            move(str(file), join(str(file.absolute().parent), new_name))

def main():
    print('Rename Date files')
    print()
    dir_path = get_dir_path()
    rename_files(dir_path, american_date_regex)

if __name__ == '__main__':
    main()