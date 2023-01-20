
def is_valid_chess_board(board_dict):
    white_pieces = {
        'king': 0,
        'pawn': 0,
        'pieces': 0
    }

    black_pieces = {
        'king': 0,
        'pawn': 0,
        'pieces': 0
    }

    for key, val in board_dict.items():
        num, letter = key
        if 1 > int(num)  or int(num) >  8:
            return False
        
        if not letter in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
            return False

        color = val[0]
        piece = val[1:]
        
        if not color in ('b', 'w'):
            return False
        
        if not piece in ('pawn', 'knight', 'bishop', 'rook', 'queen', 'king'):
            return False

        if color == 'b':
            black_pieces['pieces'] += 1
            if piece == 'king':
                black_pieces['king'] += 1
            elif piece == 'pawn':
                black_pieces['pawn'] += 1
        else:
            white_pieces['pieces'] += 1
            if piece == 'king':
                white_pieces['king'] += 1
            elif piece == 'pawn':
                white_pieces['pawn'] += 1
        
    if white_pieces['king'] > 1 or black_pieces['king'] > 1 or \
            white_pieces['pawn'] > 8 or black_pieces['pawn'] > 8: 
        return False

    return True


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