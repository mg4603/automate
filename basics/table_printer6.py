def print_table(table_data):
    col_lengths = [0] * len(table_data)
    table_height = len(table_data[0])
    table_width = len(table_data)

    for i, col in enumerate(table_data):
        col_lengths[i] = max(map(len, col))
    
    for y in range(table_height):
        for x in range(table_width):
            print(table_data[x][y].rjust(col_lengths[x]), end=' ')
        print()

def main():
    table_data = [
        ['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']
    ]
    print_table(table_data)


if __name__ == '__main__':
    main()