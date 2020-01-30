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


def show_inventory(player, board):
    '''
    for now:

    wand - 1
    potion - 2


    '''
    space_under_map = 4
    map_height = space_under_map + len(board) * 2
    inventory_height = 5
    print(f'\033[{map_height};0f' + read_box_elements(data_manager.create_map_from_file('inventory_upper')), end='')  # FIX so it depends on map size instead of 34.
    if player.wand == 1:
        print_inventory_item('wand', 1, board)
    else:
        print_inventory_item('inventory_middle_empty_cell', 1, board)
    if player.potion == 1:
        print_inventory_item('potion', 2, board)
    else:
        print_inventory_item('inventory_middle_empty_cell', 2, board)

    if player.spell == 1:
        print_inventory_item('book1', 3, board)
        print_inventory_item('inventory_middle_empty_cell', 4, board)
        print_inventory_item('inventory_middle_empty_cell', 5, board)

    elif player.spell == 2:
        print_inventory_item('book1', 3, board)
        print_inventory_item('book2', 4, board)
        print_inventory_item('inventory_middle_empty_cell', 5, board)
    elif player.spell == 3:
        print_inventory_item('book1', 3, board)
        print_inventory_item('book2', 4, board)
        print_inventory_item('book3', 5, board)
    else:
        print_inventory_item('inventory_middle_empty_cell', 3, board)
        print_inventory_item('inventory_middle_empty_cell', 4, board)
        print_inventory_item('inventory_middle_empty_cell', 5, board)

    if player.sword == 1:
        print_inventory_item('sword', 6, board)
    else:
        print_inventory_item('inventory_middle_empty_cell', 6, board)
    for i in range(0, 5):
        print_inventory_item('inventory_middle_empty_cell', (7 + i), board)  # ONLY FOR TEST PURPOSE! FIX LATER
    print(f'\033[{map_height + inventory_height};0f' + read_box_elements(data_manager.create_map_from_file('inventory_lower')))


def print_inventory_item(filename, items_obtained, board):
    space_under_map = 4
    map_height = space_under_map + len(board) * 2
    line = map_height + 1
    column = (8 * items_obtained) - 7
    with open(filename, encoding="UTF-8") as item:
        for row in item:
            print(f'\033[{line};{column}f{row}')
            line += 1


def print_table(table):
    from prettytable import PrettyTable
    tab = PrettyTable()
    tab.field_names = ['Points($)', 'Name', 'Monsters slain']
    for i in range(10):
        tab.add_row(table[i])
    print(tab)

