from helpers import *
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 80
BOARD_HEIGHT = 30


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

    def change_position(self, x_change, y_change):
        self.pos_x += x_change
        self.pos_y += y_change


def main():

    player = Player(ui.get_input('Choose a name for your character: '), PLAYER_START_X, PLAYER_START_Y, PLAYER_ICON)
    
    is_running = True
    
    while is_running:
        key = key_pressed()
        if key == 'q':
            is_running = False
        if key == 'z':
            clear_screen()
        else:
            board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
            board = engine.put_player_on_board(board, player, key)
            ui.display_board(board)


if __name__ == '__main__':
    main()