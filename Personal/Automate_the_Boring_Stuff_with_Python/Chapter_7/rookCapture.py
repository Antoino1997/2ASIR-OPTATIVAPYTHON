def white_rook_can_capture(rook_pos, board):
    rook_file = rook_pos[0]
    rook_rank = rook_pos[1]

    capturable_squares = []

    for square, piece in board.items():
        if square == rook_pos:
            continue

        target_file = square[0]
        target_rank = square[1]
        target_color = piece[0]

        if target_color == 'b':
            if target_file == rook_file or target_rank == rook_rank:
                capturable_squares.append(square)

    return capturable_squares

test_board = {
    'd7': 'bQ',
    'd2': 'wB',
    'f1': 'bP',
    'a3': 'bN'
}

result = white_rook_can_capture('d3', test_board)
print(f"The tower in d3 can capture in: {result}")