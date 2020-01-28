import data_manager
import helpers


def display_board(board):
    '''
    Displays complete game board on the screen


    Returns:
    Nothing 
    '''
    helpers.clear_screen()
    for row in board:
        print(' '.join(row))
    pass


def display_intro_screen(board):
    '''
    Displays complete intro screen board on the screen without spaces


    Returns:
    Nothing 
    '''
    helpers.clear_screen()
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
    # num_of_spaces = 10
    print('\033[34;0f' + read_box_elements(data_manager.create_map_from_file('inventory_upper')), end='') # FIX so it depends on map size instead of 34.
    if player.wand == 1:
        print_inventory_item('wand', 1)
    else:
        print_inventory_item('inventory_middle_empty_cell', 1)
    if player.potion == 1:
        print_inventory_item('potion', 2)
    else:
        print_inventory_item('inventory_middle_empty_cell', 2)
    for i in range(0, 9):
        print_inventory_item('inventory_middle_empty_cell', (3 + i))  # ONLY FOR TEST PURPOSE! FIX LATER

    # for i in range(4):
    #     if player.items > 0:
    #         line = 36 + i
    #         for j in range(1, num_of_spaces - player.items + 2):
    #             column = (player.items * 8) - 7 + 8 * j
    #             print(f'\033[{line};{column}f║       ')
    #     else:
    #         print((num_of_spaces + 1) * '║       ')
    print('\033[39;0f' + read_box_elements(data_manager.create_map_from_file('inventory_lower')))


def print_inventory_item(filename, items_obtained):
    line = 35
    column = (8 * items_obtained) - 7
    with open(filename) as item:
        for row in item:
            print(f'\033[{line};{column}f{row}')
            line += 1


def print_table(table):
    from prettytable import PrettyTable
    tab = PrettyTable()
    tab.field_names = ['Result', 'Name']
    for i in range(10):
        tab.add_row(table[i])
    print(tab)

