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
    '''
    Puts the player icon on the board on player coordinates.

    Args:
    list: The game board
    dictionary: The player information - the icon and coordinates

    Returns:
    list: The game board with the player sign on it
    '''
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

    if board[player.pos_y][player.pos_x] != '#':
        board[player.pos_y][player.pos_x] = player.icon
    else:
        player.pos_x = x_before_movement
        player.pos_y = y_before_movement
        board[player.pos_y][player.pos_x] = player.icon
    return board
