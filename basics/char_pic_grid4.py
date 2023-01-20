GRID = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]

def draw_pic_grid(grid):
    width = len(grid)
    height = len(grid[0])
    for y in range(height):
        for x in range(width):
            print(grid[x][y], end='')
        print()

if __name__ == '__main__':
    draw_pic_grid(GRID)