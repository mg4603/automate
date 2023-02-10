'''
1) take path as cmd line arg
2) get all xlsx files in the dir
3) transform all spread sheets into csv files - one per sheet
4) name csv files <file_name>_<sheet_name>.csv
'''
from argparse import ArgumentParser
from sys import exit
from pathlib import Path
from csv import writer
try:
    from openpyxl import load_workbook
except ImportError:
    exit('This program requires the openpyxl module to run.')

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('dir', help='path to dir of xlsx files to convert')
    return parser.parse_args()

def main():
    args = parse_args()

    files = get_files(args.dir)

    out_dir = Path(args.dir) / 'csvs'
    out_dir.mkdir(exist_ok=True, parents=True)

    for file in files:
        wb = load_workbook(str(file))
        sheet_names = wb.get_sheet_name()
        for sheet_name in sheet_names:
            sheet = wb.get_sheet_by_name(sheet_name)

            out_file_name = out_dir / file.stem / sheet_name / '.csv'

            print('Creating {} from {} workbook {} sheet'.format(
                out_file_name, file.stem, sheet_name
            ))
            csv_writer = writer(out_file_name)

            for row_num in range(1, sheet.max_row + 1):
                row_data = []
                for col_num in range(1, sheet.max_column + 1):
                    row_data.append(sheet.cell(row=row_num, column=col_num))
                csv_writer.writerow(row_data)
        
            csv_writer.close()

    print('Done')


if __name__ == '__main__':
    main()