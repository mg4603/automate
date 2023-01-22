'''
1) get src dir
2) get prefix
3) find missing numbers
'''

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