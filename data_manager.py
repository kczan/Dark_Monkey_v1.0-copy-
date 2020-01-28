def create_map_from_file(filename):
    board = []
    board_row = []
    with open(filename, encoding='utf-8') as map_file:
        for row in map_file:
            for element in row:
                if element == '$':
                    element = '\033[93m$\033[0m'
                board_row.append(element)
            board.append(board_row)
            board_row = []
    map_file.close()
    return board


def append_to_file(filename, table):
    with open(filename, "a+") as file:
        for element in table:
            row = element + ";"
            file.write(row)


def get_data_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table
    