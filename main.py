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
    board = data_manager.create_map_from_file('screen_title.txt')
    ui.display_intro_screen(board)
    time.sleep(3)
    board = data_manager.create_map_from_file('screen_monkey.txt')
    ui.display_intro_screen(board)
    while True:
        key = key_pressed()
        if key == ' ':
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

    def change_position(self, x_change, y_change):
        self.pos_x += x_change
        self.pos_y += y_change

    def add_money(self, amount):
        self.money += amount

    def __str__(self):
        return 'Name: {}, Gold: {}'.format(self.name, self.money)


def main():

    player = Player(ui.get_input('Choose a name for your character: '), PLAYER_START_X, PLAYER_START_Y, PLAYER_ICON)
    intro()
    is_running = True
    board = data_manager.create_map_from_file('map_one')
    ui.display_board(board)
    while is_running:
        key = key_pressed()
        if key == 'q':
            is_running = False
        if key == 'z':
            clear_screen()
        else:
            board = engine.put_player_on_board(board, player, key)
            ui.display_board(board)
            print(player)


if __name__ == '__main__':
    main()