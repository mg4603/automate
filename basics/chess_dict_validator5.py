
def main():
    board_dict = {
        '1h': 'bking', 
        '6c': 'wqueen',
        '2g': 'bbishop', 
        '5h': 'bqueen', 
        '3e': 'wking'
    }
    print(is_valid_chess_board(board_dict))

if __name__ == '__main__':
    main()