from helpers import *
import engine
import ui
import data_manager
import boss


PLAYER_ICON = '\033[96m@\033[0m'
FIRST_MAP_START_X = 3
FIRST_MAP_START_Y = 3
PLAYER_HP = 100

BOARD_WIDTH = 80
BOARD_HEIGHT = 30


class Player:

    def __init__(self, name, pos_x, pos_y, icon, hp):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp
        self.icon = icon
        self.money = 0
        self.items = 0
        self.wand = 0
        self.potion = 0
        self.spell = 0
        self.sword = 0
        self.current_map = 1
        self.key = 0
        self.message = ''
        self.hint = ''
        self.monsters_slain = 0

    def change_position(self, x_change, y_change):
        self.pos_x += x_change
        self.pos_y += y_change

    def add_money(self, amount):
        self.money += amount

    def obtained_wand(self):
        self.wand = 1
        self.items += 1

    def obtained_sword(self):
        self.sword = 1
        self.items += 1

    def obtained_magic_potion(self):
        self.potion = 1
        self.items += 1

    def obtained_spell(self):
        self.spell += 1
        self.items += 1

    def change_hp(self, amount):
        if self.hp + amount > 100:
            self.hp = 100
        else:
            self.hp += amount

    def add_key(self):
        self.key = 1

    def __str__(self):
        return f'Name: {self.name}, Gold: {self.money}'

    def result(self):
        result = [str(self.money), self.name, self.monsters_slain]
        return result

    def show_message(self):
        print(f'\033[50;0f{self.message}')

    def show_hint(self):
        print(f'\033[36;0f{self.hint}')

    def use_potion(self):
        if self.potion > 0:
            self.potion -= 1
            self.change_hp(50)
        else:
            self.message = "You don't have any potion to use!"
            self.show_message()

    def display_hp(self):
        all_bars = 10
        full_bars = int(self.hp/10)
        empty_bars = all_bars - full_bars
        print('HP: ' + full_bars * '■ ' + empty_bars * '□ ')


def intro():
    import time
    import sys
    clear_screen()
    board = data_manager.create_map_from_file('screen_title.txt')
    ui.display_intro_screen(board)
    time.sleep(3)
    clear_screen()
    board = data_manager.create_map_from_file('screen_monkey.txt')
    ui.display_intro_screen(board)
    while True:
        key = key_pressed()
        if key == 'q':
            sys.exit(0)
        elif key == 'h':
            clear_screen()
            highscore_table = sorted(data_manager.get_data_from_file("highscore.csv"), reverse=True)
            ui.print_table(highscore_table)
            if key_pressed() == 'h':
                ui.display_intro_screen(board)
        elif key == ' ':
            clear_screen()
            break


def main():
    inventory_enabled = False
    hint_enabled = False
    intro()
    current_question = engine.questions_generator(0)
    q_index = 0
    player = Player(ui.get_input('Choose a name for your character: '), FIRST_MAP_START_X, FIRST_MAP_START_Y, PLAYER_ICON, PLAYER_HP)
    is_running = True
    board = data_manager.create_map_from_file('map_one')
    board[FIRST_MAP_START_Y][FIRST_MAP_START_X] = player.icon
    ui.display_board(board)
    print(player)
    player.display_hp()
    '''engine.save_highscore(player)'''
    while is_running:
        key = key_pressed()
        if key == 'q':
            is_running = False
        if key == 'z':
            clear_screen()
        if key == 'i':
            if not inventory_enabled:
                player.display_hp()
                ui.show_inventory(player, board)
                inventory_enabled = True
                hint_enabled = False
            else:
                ui.display_board(board)
                print(player)
                inventory_enabled = False
        if key == 'k':
            if not hint_enabled:
                ui.display_board(board)
                print(player)
                player.display_hp()
                player.show_hint()
                hint_enabled = True
                inventory_enabled = False
            else:
                ui.display_board(board)
                print(player)
                hint_enabled = False
        if key == 'u':
            player.use_potion()
            ui.display_board(board)
            print(player)
            player.display_hp()
            if inventory_enabled:
                ui.show_inventory(player, board)
        if key in ['w', 'a', 's', 'd']:
            player.message = ''
            board, current_question, q_index = engine.put_player_on_board(board, player, key, player.current_map, current_question, q_index)
            ui.display_board(board)
            print(player)
            player.display_hp()
            player.show_message()
            if inventory_enabled:
                ui.show_inventory(player, board)
        if player.hp <= 0:
            is_running = False
            boss.display_screen('lose.txt')


if __name__ == '__main__':
    main()