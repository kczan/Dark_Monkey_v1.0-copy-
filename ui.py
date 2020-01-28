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
