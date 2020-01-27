def create_map_from_file(filename):
    board = []
    board_row = []
    with open(filename) as map_file:
        for row in map_file:
            for element in row:
                board_row.append(element)
            board.append(board_row)
            board_row = []
    map_file.close()
    return board
