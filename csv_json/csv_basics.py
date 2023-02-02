from csv import reader, writer, DictReader, DictWriter
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

def tsv(filename):
    with Path(filename).open('w') as file:
        example_writer = writer(
            file, delimiter='\t', lineterminator='\n\n'
        )
        example_writer.writerow(['apples', 'oranges', 'grapes'])
        example_writer.writerow(['eggs', 'bacon', 'ham'])
        example_writer.writerow(
            ['spam', 'spam', 'spam', 'spam', 'spam', 'spam']
        )

def read_with_dictreader(filename):
    with Path(filename).open('r') as file:
        example_reader = DictReader(file)
        for row in example_reader:
            print(row['Timestamp'], row['Fruit'], row['Quantity'])

def dictreader_no_header(filename):
    with Path(filename).open('r') as file:
        example_reader = DictReader(file, ['time', 'name', 'amount'])
        for row in example_reader:
            print(row['time'], row['name'], row['amount'])

def write_with_dictwriter(filename):
    with Path(filename).open('w') as file:
        example_writer = DictWriter(file, ['Name', 'Pet', 'Phone'])
        example_writer.writeheader()
        example_writer.writerow({
            'Name': 'Alice',
            'Pet': 'cat',
            'Phone': '555-1234'
            })
        example_writer.writerow({
            'Name': 'Bob',
            'Phone': '555-9999'
        })
        example_writer.writerow({
            'Phone': '555-5555',
            'Name': 'Carol',
            'Pet': 'dog'
        })

# write_with_dictwriter('dict_writer_output.csv')
# dictreader_no_header('example.csv')
# read_with_dictreader('examples_with_header.csv')
# tsv('example.tsv')
# write_csv('output.csv')
# read_with_for_loop('example.csv')
# print(csv_as_list('example.csv'))