"""
Koc University, Turkey
KOLT Python Certificate Program
Spring 2020 - Assignment 1
Created by @ahmetuysal and @hasancaslan
"""

import turtle

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
PEN_SIZE = 5
SQUARE_SIZE = 100
ANIMATION_SPEED = 100    # Animation speed

def draw_empty_board():
    """
    This function should draw the empty tic-tac-toe board using turtle module
    """
    # TODO: Implement this function
    # Hints:
    # 1- You might want to implement a helper function for drawing only one square
    # 2- You can create a "nested" for loop to draw a 3x3 board using the helper function you created


def draw_x_in_square(row, column):
    """
    This function should draw and X symbol on the given square of tic-tac-toe board
    """
    # TODO: Implement this function
    # Hints:
    # 1- You might want to use penup, pendown, setpos, setheading, forward functions from turtle module
    # 2- We recommend you to spend some time with turtle module in the interactive shell to understand
    # how it uses coordinates (which directions are positive, which angles correspond to which directions, etc.)
    pass


def draw_o_in_square(row, column):
    """
    This function should draw and O symbol on the given square of tic-tac-toe board
    """
    # TODO: Implement this function
    # Hints:
    # 1- You might want to use penup, pendown, setpos, setheading, circle functions from turtle module
    # 2- We recommend you to spend some time with turtle module in the interactive shell to understand
    # how it uses coordinates (which directions are positive, which angles correspond to which directions, etc.)
    pass

def display_setup():
    turtle.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
    turtle.speed(ANIMATION_SPEED)
    turtle.pensize(PEN_SIZE)


if __name__ == '__main__':
    # Display setup
    display_setup()
    draw_empty_board()

    player_names = []
    # TODO: Take player names, any string other than empty string is considered a valid name

    # Game setup
    game = [['', '', ''], ['', '', ''], ['', '', '']]

    # Loop for the game
    for move_counter in range(9):
        # TODO: Get current user to play
        current_player_name = ''

        # TODO: take user's move
        move = ''

        # TODO: validate the user's move, you need to ask again until user enters a valid move
        # 1. It should be a string consisting of two parts (Hint: use "string".split(' ') function)
        # 2. Both its parts should be integers (Hint: "string".isnumeric() function)
        # 3. Integers should be in range [0, 2] inclusive
        # 4. Selected square should be emtpy

        # TODO: play the move: you should modify the game list & display the move using turtle

        there_is_winner = False
        # TODO: check win conditions

        # If there is a winner, terminate loop
        # and display winner
        if there_is_winner:
            print(f'{current_player_name} wins!')
            break

    # If there_is_winner variable is still false, game ended in a draw
    if not there_is_winner:
        print('Game ended in a draw')

    turtle.done()
