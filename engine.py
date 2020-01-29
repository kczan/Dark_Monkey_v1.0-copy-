import data_manager


def create_board(width, height):

    map_list = []
    map_row = []
    for _ in range(width):
        map_row.append('#')
    map_list.append(map_row)
    map_row = []
    for _ in range(height):
        map_row.append('#')
        for _ in range(width - 2):
            map_row.append('.')
        map_row.append('#')
        map_list.append(map_row)
        map_row = []
    for _ in range(width):
        map_row.append('#')
    map_list.append(map_row)
    return map_list


def keep_player_still(player, x_before_movement, y_before_movement, board):
    player.pos_x = x_before_movement
    player.pos_y = y_before_movement
    board[player.pos_y][player.pos_x] = player.icon
    return board


def wipe_element(board, pos_x, pos_y, player):
    board[player.pos_y][player.pos_x] = player.icon
    board[pos_y][pos_x] = '.'


def put_player_on_board(board, player, key, current_map):

    x_before_movement = player.pos_x
    y_before_movement = player.pos_y
    left_doors_x = 46
    left_doors_y = 1
    right_doors_x = 1
    right_doors_y = 1

    if key == 'w':
        player.change_position(0, -1)
    elif key == 's':
        player.change_position(0, 1)
    elif key == 'a':
        player.change_position(-1, 0)
    elif key == 'd':
        player.change_position(1, 0)

    if board[player.pos_y][player.pos_x] not in ('#', '\033[92m#\033[0m', '|'):
        temp = check_field(board[player.pos_y][player.pos_x], player, current_map, x_before_movement, y_before_movement, board)
        if temp:
            board = data_manager.create_map_from_file(data_manager.get_map_name_from_list(temp))
            if player.pos_x > 40:
                board[right_doors_y][right_doors_x] = player.icon
                player.pos_x = right_doors_x
                player.pos_y = right_doors_y
            elif player.pos_x < 40:
                board[left_doors_y][left_doors_x] = player.icon
                player.pos_x = left_doors_x
                player.pos_y = left_doors_y
        board[player.pos_y][player.pos_x] = player.icon
        board[y_before_movement][x_before_movement] = '.'
    elif board[player.pos_y][player.pos_x] == '|':
        if player.key == 0:
            board = keep_player_still(player, x_before_movement, y_before_movement, board)
            print('\033[50;0fDUPA')
        else:
            board[player.pos_y][player.pos_x] = player.icon
            board[y_before_movement][x_before_movement] = '.'
            player.key = 0
    else:
        board = keep_player_still(player, x_before_movement, y_before_movement, board)

    return board


def check_field(symbol, player, current_map, player_x, player_y, board):
    GOLD_FOUND = 100

    if symbol == '\033[93m$\033[0m':
        player.add_money(GOLD_FOUND)
    elif symbol == '?':
        if question_mark("Password please!", "111"):
            player.key = 1
    elif symbol == 'K':
        pass
    elif symbol == 'î':
        player.obtained_wand()
    elif symbol == 'Ô':
        player.obtained_magic_potion()
    elif symbol == 'S':
        player.obtained_spell()
    elif symbol == '¥':
        player.add_key()
    elif symbol == '>':
        return data_manager.switch_map(current_map, 'next', player)
    elif symbol == '<':
        return data_manager.switch_map(current_map, 'previous', player)
    return False


def save_highscore(player):
    import data_manager
    result = player.result()
    data_manager.append_to_file("highscore.csv", result)


def question_mark(question, answer):
    import ui
    user_answer = ui.get_input(question)
    if user_answer == answer:
        return True
    else:
        return False
