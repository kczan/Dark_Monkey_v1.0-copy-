def create_map_from_file(filename):
    board = []
    board_row = []
    with open(filename, encoding='utf-8') as map_file:
        for row in map_file:
            for element in row:
                if element == '$':
                    element = '\033[93m$\033[0m'
                elif element == '^':
                    element = '\033[94m^\033[0m'
                elif element == '#' and filename == 'map_two.txt':
                    element = '\033[92m#\033[0m'
                board_row.append(element)
            board.append(board_row)
            board_row = []
    map_file.close()
    return board


def append_to_file(filename, table):
    from csv import writer
    with open(filename, "a+", newline = '') as file:
        csv_writer = writer(file)
        csv_writer.writerow(table)


def get_data_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(",") for element in lines]
    for row in table:
        row[0] = int(row[0])
    return table
    