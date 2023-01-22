'''
1) get directory/ file to backup
2) get destination dir
3) check if backup exists in destination
4) check number on backup if it exists
5) create next numbered backup
'''
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from os import walk
from os.path import basename, join

def get_zip_src():
    print('Enter file or directory to backup:')
    while True:
        name = input('> ')
        if Path(name).exists():
            return Path(name)
        print('No such file or directory exists.')

def create_backup(path, destination_path):
    file_to_backup = str(path.absolute().name)
    i = 1
    while True:
        zip_file_name = '{}_{}.zip'.format(file_to_backup, i)
        zip_file_path = destination_path / zip_file_name
        if not zip_file_path.exists():
            break
        i += 1
    
    print('Creating new zip file {}'.format(str(zip_file_path.name)))

    with ZipFile(zip_file_path, 'w') as f:
        for folder_name, _, file_names in walk(path.absolute()):
            f.write(folder_name)
            for file_name in file_names:
                new_base = basename(folder_name) + '_'
                if file_name.startswith(new_base) and file_name.endswith('.zip'):
                    continue
                f.write(join(folder_name, file_name))

def main():
    print('Backup to Zip')
    print()
    path = get_zip_src()
    print('Enter directory to write backup to:')
    destination_name = input('> ')
    destination_path = Path(destination_name)
    destination_path.mkdir(
        parents=True, exist_ok=True
    )
    create_backup(path, destination_path)
    print('Backup created.')

if __name__ == '__main__':
    main()