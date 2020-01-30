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
    '''
    Function too big, let's try to divide it into smaller ones if we can.
    '''
    x_before_movement = player.pos_x
    y_before_movement = player.pos_y
    left_doors_x = 46
    left_doors_y = 1
    right_doors_x = 1
    right_doors_y = 1
    OBSTACLE_SYMBOLS = ['#', '\033[92m#\033[0m', '|', 'K', 'T']
    MONSTER_SYMBOLS = ['K', 'T']

    if key == 'w':
        player.change_position(0, -1)
    elif key == 's':
        player.change_position(0, 1)
    elif key == 'a':
        player.change_position(-1, 0)
    elif key == 'd':
        player.change_position(1, 0)

    if board[player.pos_y][player.pos_x] not in OBSTACLE_SYMBOLS:
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
    elif board[player.pos_y][player.pos_x] in MONSTER_SYMBOLS:
        board = fight_monster(board[player.pos_y][player.pos_x], board, player, x_before_movement, y_before_movement)
    elif board[player.pos_y][player.pos_x] == '|':
        if player.key == 0:
            board = keep_player_still(player, x_before_movement, y_before_movement, board)
        else:
            board[player.pos_y][player.pos_x] = player.icon
            board[y_before_movement][x_before_movement] = '.'
            player.key = 0
    else:
        board = keep_player_still(player, x_before_movement, y_before_movement, board)

    return board


def check_field(symbol, player, current_map, player_x, player_y, board):
    GOLD_FOUND = 100
    TRAP = 20

    if symbol == '\033[93m$\033[0m':
        player.add_money(GOLD_FOUND)
    elif symbol == '?':
        if question_mark(player, "Password please!", "111"):
            player.key = 1
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
    elif symbol == '\033[91mx\033[0m':
        player.change_hp(TRAP)
    return False


def save_highscore(player):
    import data_manager
    result = player.result()
    data_manager.append_to_file("highscore.csv", result)


def question_mark(player, question, answer):
    import ui
    REWARD = 200
    user_answer = ui.get_input(question)
    if user_answer == answer:
        ui.print_message("Correct!")
        player.add_money(REWARD)
        return True
    else:
        ui.print_message("Wrong!")
        return False


def fight_monster(symbol, board, player, x_before_movement, y_before_movement):
    if symbol == 'K':  # skeleton, weak to wand spells
        if player.wand == 1:
            board[player.pos_y][player.pos_x] = player.icon
            board[y_before_movement][x_before_movement] = '.'
        else:
            board = keep_player_still(player, x_before_movement, y_before_movement, board)
            player.message = 'To defeat the skeleton, you need some kind of magic item!'
            player.show_message()
    return board
