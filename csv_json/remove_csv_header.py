'''
1) find all csv files in the cwd
2) read csv files
3) remove headers 
4) write to new folder
'''
from argparse import ArgumentParser
from csv import reader, writer
from pathlib import Path
from sys import exit
from logging import debug, disable, basicConfig, DEBUG, CRITICAL

basicConfig(
    level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s'
)
disable(CRITICAL)

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('file', help='csv file to remove header of')
    parser.add_argument(
        '-o', '--output-path', help='output path of header less file'
    )
    return parser.parse_args()

def main():
    args = parse_args()
    print('Remove Csv Header')
    print()
    file_name = args.file
    file_path = Path(file_name)
    if not file_path.exists():
        exit('File Does Not Exist: {}'.format(file_name))
    
    debug(args.output_path)
    output_path_name = args.output_path
    if not args.output_path:
        debug(1)
        output_path_name = file_path.stem + '_no_header.csv'
    
    output_path = Path(output_path_name)
    debug(output_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open('r') as input_file:
        file_reader = reader(input_file)
        
        with output_path.open('w') as output_file:
            file_writer = writer(output_file)
            for row in file_reader:
                if file_reader.line_num == 1:
                    continue
                debug('Row #{} {}'.format(file_reader.line_num, row))
                file_writer.writerow(row)
    
    print('Done')

            

if __name__ == '__main__':
    main()