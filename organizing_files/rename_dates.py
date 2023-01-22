'''
1) get files in user defined dir
2) Id files with names in european date style
3) rename files to american date style
'''

def main():
    print('Rename Date files')
    print()
    dir_path = get_dir_path()
    rename_files(dir_path, american_date_regex)

if __name__ == '__main__':
    main()