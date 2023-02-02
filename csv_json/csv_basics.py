from csv import reader, writer
from pathlib import Path

def csv_as_list(filename):
    with Path(filename).open('r') as file:
        csv_reader = reader(file)
        csv_data_as_list = list(csv_reader)
        return csv_data_as_list

def read_with_for_loop(filename):
    with Path(filename).open('r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            print('Row #{} {}'.format(csv_reader.line_num, row))

def write_csv(filename):
    with Path(filename).open('w', newline='') as file:
        csv_writer = writer(file)
        csv_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
        csv_writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
        csv_writer.writerow([1, 2, 3.141592, 4])

# write_csv('output.csv')
# read_with_for_loop('example.csv')
# print(csv_as_list('example.csv'))