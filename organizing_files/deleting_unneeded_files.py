'''
1) get source dir
2) walk dir
3) check size of files in dir
4) list files larger than 100mb
'''
from pathlib import Path
from os import walk
from os.path import join

def get_src_path():
    print('Enter source directory path to check for large files:')
    while True:
        dir_name = input('> ')
        dir_path = Path(dir_name)
        if dir_path.exists():
            if dir_path.is_dir():
                return dir_path
            print('Entered path doesn\'t point to a directory.')
        else:
            print('Directory doesn\'t exist.')


def main():
    print('Finding Large Files')
    print()
    src_path = get_src_path()
    large_files = []
    for folder_name, _, file_names in walk(src_path.absolute()):
        for file_name in file_names:
            file = Path(join(folder_name, file_name))
            try:
                if file.stat().st_size // (1024 * 1024) > 100:
                    large_files.append(str(file.absolute()))
            except:
                pass
    
    if len(large_files) > 0:
        print('Files larger than 100MB:')
        print('\n'.join(large_files))
    else:
        print('No large files found.')
    print('Done')

if __name__ == '__main__':
    main()