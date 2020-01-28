import data_manager


def display_board(board):
    '''
    Displays complete game board on the screen


    Returns:
    Nothing 
    '''
    import os
    os.system('clear')
    os.system('cls')
    for row in board:
        print(' '.join(row))
    pass


def display_intro_screen(board):
    '''
    Displays complete intro screen board on the screen without spaces


    Returns:
    Nothing 
    '''
    import os
    os.system('clear')
    os.system('cls')
    for row in board:
        print(''.join(row), end ="")
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
    '''
    for now:

    wand - 1
    potion - 2


    '''
    num_of_spaces = 10
    print(read_box_elements(data_manager.create_map_from_file('inventory_upper')), end='')
    if player.wand == 1:
        print_inventory_item('wand', 1)
    else:
        print_inventory_item('inventory_middle_empty_cell', 1)
    if player.potion == 1:
        print_inventory_item('potion', 2)
    else:
        print_inventory_item('inventory_middle_empty_cell', 2)
    for i in range(0, 9):
        print_inventory_item('inventory_middle_empty_cell', 3 + i)  # ONLY FOR TEST PURPOSE! FIX LATER
    # for i in range(4):
    #     if player.items > 0:
    #         line = 36 + i
    #         for j in range(1, num_of_spaces - player.items + 2):
    #             column = (player.items * 8) - 7 + 8 * j
    #             print(f'\033[{line};{column}f║       ')
    #     else:
    #         print((num_of_spaces + 1) * '║       ')
    print('\033[40;0f' + read_box_elements(data_manager.create_map_from_file('inventory_lower')))


def print_inventory_item(filename, items_obtained):
    line = 36
    column = (8 * items_obtained) - 7
    # print(f'{line} | {column}')
    with open(filename) as item:
        for row in item:
            print(row, end='')
        print('\r')
        print(f'\033[{line};{column}f{row}')
        line += 1

def print_table(table):
    from prettytable import PrettyTable
    tab = PrettyTable()
    tab.field_names = ['Result','Name']
    for i in range(10):
        tab.add_row(table[i])
    print(tab)

