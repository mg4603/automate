'''
1) get src dir
2) get prefix
3) find missing numbers
'''

from pathlib import Path
from re import sub, compile

def get_src_dir():
    print('Enter directory to search:')
    src_dir_name = input('> ')
    src_dir_path = Path(src_dir_name).absolute()
    if src_dir_path.exists():
        if src_dir_path.is_dir():
            return src_dir_path
        print('{} isn\'t a directory.'.format(src_dir_path.name))
    else:
        print('{} doesn\'t exist.'.format(src_dir_path.name))

def get_gaps(files):
    regex = compile(r'(\D*)(\d+)(\D*)')

    mo = regex.search(files[0])
    prefix = mo.group(1)
    suffix = mo.group(3)

    files = [sub(r'\D*(\d+)\D*', r'\1',  file) for file in files]
    files = list(map(int, files))
    files.sort()

    gaps = []
    idx = files[0]
    for file in files:
        if file == idx:
            idx += 1
        else:
            gaps.append(idx)
            idx += 1
    
    digits = len(str(files[-1]))

    return [
        '{}{}{}'.format(
            prefix,
            str(gap).zfill(digits),
            suffix
        ) for gap in gaps
    ]

def main():
    print('Filling in the Gaps')
    print()
    src_dir_path = get_src_dir()

    print('Enter prefix to search for:')
    prefix = input('> ')

    print()
    print('Starting')
    print()
    files = src_dir_path.glob('*')
    files = [file.name for file in files if prefix in file.name]
    gaps = get_gaps(files)
    if gaps:
        print('Missing files:')
        print('\n'.join(gaps))
    else:
        print('No gap files found.')
    print()
    print('Done')

if __name__ == '__main__':
    main()