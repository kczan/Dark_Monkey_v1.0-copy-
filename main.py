from helpers import *
import engine
import ui
import data_manager

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 80
BOARD_HEIGHT = 30


def intro():
    import time
    import sys
    board = data_manager.create_map_from_file('screen_title.txt')
    ui.display_intro_screen(board)
    time.sleep(3)
    board = data_manager.create_map_from_file('screen_monkey.txt')
    ui.display_intro_screen(board)
    while True:
        key = key_pressed()
        if key == 'q':
            sys.exit(0)
        elif key == ' ':
            break


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {}
    player["x"] = PLAYER_START_X
    player["y"] = PLAYER_START_Y
    player["icon"] = PLAYER_ICON
    return player


class Player:

    def __init__(self, name, pos_x, pos_y, icon):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.icon = icon
        self.money = 0
        self.items = 0
        self.wand = 0
        self.wand_printed = False
        self.potion = 0
        self.potion_printed = False

    def change_position(self, x_change, y_change):
        self.pos_x += x_change
        self.pos_y += y_change

    def add_money(self, amount):
        self.money += amount

    def obtained_wand(self):
        self.wand = 1
        self.items += 1

    def obtained_magic_potion(self):
        self.potion = 1
        self.items += 1

    def __str__(self):
        return 'Name: {}, Gold: {} Items: {}'.format(self.name, self.money, self.items)

    def result(self):
        result = [str(self.money), self.name]
        return result


def main():
    inventory_enabled = False
    intro()
    player = Player(ui.get_input('Choose a name for your character: '), PLAYER_START_X, PLAYER_START_Y, PLAYER_ICON)
    is_running = True
    board = data_manager.create_map_from_file('map_one')
    ui.display_board(board)
    print(player)
    engine.save_highscore(player) #test
    highscore_table = sorted(data_manager.get_data_from_file("highscore.csv")) #test
    ui.print_table(highscore_table) #test
    while is_running:
        key = key_pressed()
        if key == 'q':
            is_running = False
        if key == 'z':
            clear_screen()
        if key == 'i':
            if not inventory_enabled:
                ui.show_inventory(player)
                inventory_enabled = True
            else:
                ui.display_board(board)
                print(player)
                inventory_enabled = False
        else:
            board = engine.put_player_on_board(board, player, key)
            ui.display_board(board)
            print(player)
            if inventory_enabled:
                ui.show_inventory(player)


if __name__ == '__main__':
    main()