import os
import random
import time
import sys
import helpers


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_boss(): 
    with open('boss.txt') as f:
        read_data = f.read()
    print('\033[91m' + read_data + '\033[0m') 


def play_cold_warm():
    user_guesses = 10
    correct_answer = generate_unique_number()

    while user_guesses > 0:
        user_input = get_user_input()
        feedback = compare_user_answer(user_input, correct_answer)
        print('MAUPA: ', end='')
        helpers.clear_screen()
        display_boss()
        for i in feedback:
            print(i, end=' ')
        print('Guesses left:', user_guesses - 1)

        if feedback == ['hot']:
            display_screen('win.txt')
            time.sleep(3)
            sys.exit()
        user_guesses -= 1

        if user_guesses == 0:
            display_screen('lose.txt')
            sys.exit()


def get_user_input():
    while True:  
        user_input = input('Enter unique number: ')
        if user_input.isdigit() and len(user_input) == 1 and len(set(user_input)) == len(user_input):
            break
        else:
            print('ErrrRRoorNumber have 1 unique digits!')
    return list(user_input)


def display_screen(filename):
    clear_console()
    with open(filename) as f:
        read_data = f.read()
    print(read_data)


def compare_user_answer(guess, correct_answer):
    hints = []
    for i in range(len(guess)):
        if guess[i] == correct_answer[i]:
            hints.insert(0, 'hot')
        elif guess[i] in correct_answer:
            hints.append('warm')
    if not hints:
        hints = ['cold']
    return hints


def generate_unique_number():
    unique_number_list = [str(x) for x in range(10)]
    random.shuffle(unique_number_list)
    return unique_number_list[:3]


def start_fight():
    helpers.clear_screen()
    display_boss()

    while True:
        answer = input('fight?').lower()
        helpers.clear_screen()
        display_boss()
        if answer == 'yes':
            print('BOSS: lets play cold/warm/hot! you have 10 guesses name the number? ')
            play_cold_warm()
            break


if __name__ == '__main__':
    start_fight()