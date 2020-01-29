
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
    

def put_player_on_board(board, player, key):

    x_before_movement = player.pos_x
    y_before_movement = player.pos_y

    if key == 'w':
        player.change_position(0, -1)
    elif key == 's':
        player.change_position(0, 1)
    elif key == 'a':
        player.change_position(-1, 0)
    elif key == 'd':
        player.change_position(1, 0)

    if board[player.pos_y][player.pos_x] != ('#' and '\033[92m#\033[0m'):
        check_field(board[player.pos_y][player.pos_x], player)
        board[player.pos_y][player.pos_x] = player.icon
        board[y_before_movement][x_before_movement] = '.'
    else:
        player.pos_x = x_before_movement
        player.pos_y = y_before_movement
        board[player.pos_y][player.pos_x] = player.icon

    return board


def check_field(symbol, player):
    GOLD_FOUND = 100

    if symbol == '\033[93m$\033[0m':
        player.add_money(GOLD_FOUND)
    elif symbol == '?':
        result = question_mark("Password please!", "111")
        if result == True:
            pass
    elif symbol == 'K':
        pass
    elif symbol == 'î':
        player.obtained_wand()
    elif symbol == 'Ô':
        player.obtained_magic_potion()
    elif symbol == 'S':
        player.obtained_spell()


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