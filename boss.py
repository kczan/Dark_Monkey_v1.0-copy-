import random
import time
import sys
import helpers
import ui


def display_boss(): 
    with open('boss.txt') as f:
        read_data = f.read()
    print('\033[91m' + read_data + '\033[0m') 


def play_cold_warm():
    user_guesses = 10
    correct_answer = random.choice(range(21))

    while user_guesses > 0:
        user_input = ui.get_input("What's your guess? ")
        result = compare_user_answer(user_input, correct_answer)
        time.sleep(1)
        helpers.clear_screen()
        display_boss()
        if result:
            print('You have defeated me... Pure luck!')
            time.sleep(3)
            display_screen('win.txt')
            break
        user_guesses -= 1
        print('Guesses left:', user_guesses)

        if user_guesses == 0:
            display_screen('lose.txt')
            sys.exit(0)


def display_screen(filename):
    helpers.clear_screen()
    with open(filename) as f:
        read_data = f.read()
    print(read_data)


def compare_user_answer(guess, correct_answer):
    if int(guess) < int(correct_answer):
        print('Too low! Try again.')
        return False
    elif int(guess) > int(correct_answer):
        print('Too high!')
        return False
    else:
        return True


def start_fight(player):
    helpers.clear_screen()
    display_boss()

    while True:
        helpers.clear_screen()
        display_boss()
        print('BOSS: lets play High/Low! You have 10 chances to guess my number from 0 to 20. ')
        play_cold_warm()
        print(player)
        break
