def get_map_name_from_list(index):
    with open('map_list') as map_file:
        print(index)
        for row in map_file:
            list_index, map_name = row.split('|')
            map_name = map_name.rstrip('\n')
            if list_index == str(index):
                return map_name
        return "FALSE MAP FILE"


def create_map_from_file(filename):
    board = []
    board_row = []
    with open(filename, encoding='utf-8') as map_file:
        for row in map_file:
            for element in row:
                if element == '$':
                    element = '\033[93m$\033[0m'
                elif element == '¶':
                    element = '\033[94m¶\033[0m'
                elif element == ',':
                    element = '\033[92m,\033[0m'
                elif element == 'x':
                    element = '\033[91mx\033[0m'
                elif element == '~':
                    element = '\033[94m~\033[0m'
                elif element == '*':
                    element = '\033[95m*\033[0m'
                board_row.append(element)
            board.append(board_row)
            board_row = []
    map_file.close()
    return board


def append_to_file(filename, table):
    from csv import writer
    with open(filename, "a+", newline='\n') as file:
        csv_writer = writer(file)
        csv_writer.writerow(table)


def get_data_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(",") for element in lines]
    for row in table:
        row[0] = int(row[0])
    return table


def switch_map(current_map, direction, player):
    if direction == 'previous':
        player.current_map = current_map - 1
        return player.current_map
    elif direction == 'next':
        player.current_map = current_map + 1
        return player.current_map


def get_questions(filename):
    with open(filename, "r") as questions_file:
        lines = questions_file.readlines()
        questions = [element.replace("\n", "").split(";") for element in lines]
        return questions
