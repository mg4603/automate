'''
1) get directory/ file to backup
2) get destination dir
3) check if backup exists in destination
4) check number on backup if it exists
5) create next numbered backup
'''
from pathlib import Path

def main():
    print('Backup to Zip')
    print()
    path = get_path_backup()
    print('Enter directory to write backup to:')
    destination_name = input('> ')
    destination_path = Path(
        destination_name
    ).mkdir(
        parents=True, exist_ok=True
    )
    create_backup(path, destination_path)
    print('Backup created.')

if __name__ == '__main__':
    main()