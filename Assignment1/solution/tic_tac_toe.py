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
    for row_no in range(3):
        for col_no in range(3):
            turtle.penup()
            turtle.setpos(SQUARE_SIZE * (row_no - 1.5),
                          SQUARE_SIZE * (col_no - 1.5))
            turtle.pendown()
            draw_square()


def draw_square():
    for i in range(4):
        turtle.forward(SQUARE_SIZE)
        turtle.left(90)


def draw_x_in_square(row, column):
    turtle.penup()
    # go to the bottom left corner of square (x, y)
    turtle.setpos(SQUARE_SIZE * (column - 1.5), SQUARE_SIZE * (0.5 - row))
    turtle.setheading(45)
    turtle.pendown()
    turtle.forward(SQUARE_SIZE * 2**(1 / 2))
    turtle.penup()
    # go to the top left corner of square (x, y)
    turtle.setpos(SQUARE_SIZE * (column - 1.5), SQUARE_SIZE * (1.5 - row))
    turtle.setheading(315)
    turtle.pendown()
    turtle.forward(SQUARE_SIZE * 2**(1 / 2))


def draw_o_in_square(row, column):
    turtle.penup()
    turtle.setheading(0)
    # go to the bottom center of square (x, y)
    turtle.setpos(SQUARE_SIZE * (column - 1), SQUARE_SIZE * (0.5 - row))
    turtle.pendown()
    turtle.circle(SQUARE_SIZE * 0.5)


def display_player_move(player, row, column):
    if player == 1:
        draw_x_in_square(row, column)
    else:
        draw_o_in_square(row, column)


if __name__ == '__main__':
    # Display setup
    turtle.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
    turtle.speed(ANIMATION_SPEED)
    turtle.pensize(PEN_SIZE)
    draw_empty_board()
    print(turtle.pos())

    # TODO: Take player names, any string other than empty string is considered a valid name
    player_names = []

    for i in range(2):
        player_name = input(f'Player {i + 1}, please enter your name: ')
        while not player_name:
            player_name = input(f'Player {i + 1}, please enter a valid name: ')
        player_names.append(player_name)

    # Game setup
    game = [['', '', ''], ['', '', ''], ['', '', '']]

    # Loop for the game
    for move_counter in range(9):
        # TODO: take user's move
        player_name = player_names[move_counter % len(player_names)]
        move = input(
            f'{player_name}, which row and column? (0-based, seperated with a space i.e. "0 1"): ').strip().split(' ')
        # TODO: validate the user's move, you need to ask again until user enters a valid move
        # 1. It should be a string consisting of two parts (Hint: use "string".split(' ') function)
        # 2. Both its parts should be integers (Hint: "string".isnumeric() function)
        # 3. Integers should be in range [0, 2] inclusive
        # 4. Selected square should be emtpy
        while (len(move) != 2 or not move[0].isnumeric()
               or not move[1].isnumeric() or not (0 <= int(move[0]) <= 2)
               or not (0 <= int(move[1]) <= 2) or game[int(move[0])][int(move[1])] != ''):
            move = input(
                'Please enter a valid move? (0-based, seperated with a space i.e. "0 1"): ').strip().split(' ')

        # TODO: play the move
        if move_counter % 2 == 0:
            game[int(move[0])][int(move[1])] = 'X'
            draw_x_in_square(int(move[0]), int(move[1]))
        else:
            game[int(move[0])][int(move[1])] = 'O'
            draw_o_in_square(int(move[0]), int(move[1]))

        # TODO: check win conditions
        there_is_winner = False
        game_slices = []

        for index in range(3):
            row = game[index]
            col = [game[0][index], game[1][index], game[2][index]]
            game_slices.append(row)
            game_slices.append(col)

        down_diagonal = [game[0][0], game[1][1], game[2][2]]
        up_diagonal = [game[0][2], game[1][1], game[2][0]]
        game_slices.append(down_diagonal)
        game_slices.append(up_diagonal)

        for game_slice in game_slices:
            if (game_slice[0] != '' and game_slice[0] == game_slice[1]
                    and game_slice[1] == game_slice[2]):
                there_is_winner = True
                break

        # If there is a winner, terminate loop
        # and display winner else continue game
        if there_is_winner:
            print(f'{player_name} wins!')
            break

    if not there_is_winner:
        print('Game ended in a draw')

    turtle.done()
