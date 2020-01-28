import data_manager


def display_board(board):
    '''
    Displays complete game board on the screen


    Returns:
    Nothing 
    '''
    import os
    os.system('clear')
    for row in board:
        print(' '.join(row))
    pass


def get_input(input_prompt):
    '''

    Args:
        input_prompt: A question for the user.

    Returns:
        input_string: A string that contains user's response.
    '''
    input_string = input(input_prompt)
    return input_string


def print_message(message):
    print(message)


def read_box_elements(element):
    for row in element:
        return ''.join(row)


def show_inventory(player):
    num_of_spaces = 10
    print(read_box_elements(data_manager.create_map_from_file('inventory_upper')), end='')
    if player.wand == 1:
        print('║  ')
    for _ in range(3):
        print((num_of_spaces - player.items) * '║       ', end='')
        print('║   ')
    print(read_box_elements(data_manager.create_map_from_file('inventory_lower')))


