'''
1) get src dir
2) get prefix
3) find missing numbers
'''

from pathlib import Path

def get_src_dir():
    print('Enter directory to search:')
    src_dir_name = input('> ')
    src_dir_path = Path(src_dir_name).absolute()
    if src_dir_path.exist():
        if src_dir_path.is_dir():
            return src_dir_path
        print('{} isn\'t a directory.'.format(src_dir_path.name))
    else:
        print('{} doesn\'t exist.'.format(src_dir_path.name))

def main():
    print('Filling in the Gaps')
    print()
    src_dir_path = get_src_dir()

    print('Enter prefix to search for:')
    prefix = input('> ')

    print('Starting:')
    files = src_dir_path.glob('*')
    files = [file.name for file in files if prefix in file.name]
    gaps = get_gaps(files)
    if gaps:
        print('Missing files:')
        print('\n'.join(gaps))
    else:
        print('No gap files found.')

    print('Done')

if __name__ == '__main__':
    main()