from computer_player import *
from time import sleep
from collections import deque

green = "\033[0;32m"
red = "\033[0;31m"
nocolor = "\033[0m"


def player_move(matrix, player):
    if player == 1:
        color = green
    else:
        color = red

    while True:
        player_input = input(color + f'Player {player}, choose a column:\n')
        try:
            player_input = int(player_input)
        except ValueError:
            print('Please use numeric digits.')
            continue
        if player_input > len(matrix[0]):
            print('Invalid choice!')
            continue
        matrix_column = player_input - 1
        for row in range(len(matrix)-1, -1, -1):
            if matrix[row][matrix_column] == 0:
                matrix[row][matrix_column] = player
                break
        else:
            print('Invalid choice!')
            continue
        break


def check_win_horizontal(matrix, player):
    for row in matrix:
        for column in range(len(row)-3):
            if row[column: column+4] == 4*[player]:
                return True


def check_win_vertical(matrix, player):
    for row in range(len(matrix)-3):
        for column in range(len(matrix[row])):
            four_vertical = [matrix[row][column],
                             matrix[row+1][column],
                             matrix[row+2][column],
                             matrix[row+3][column]]
            if four_vertical == 4*[player]:
                return True


def check_win_right_diagonal(matrix, player):
    for row in range(len(matrix)-3):
        for column in range(len(matrix[row])-3):
            four_right_diag = [matrix[row][column],
                               matrix[row + 1][column+1],
                               matrix[row + 2][column+2],
                               matrix[row + 3][column+3]]
            if four_right_diag == 4*[player]:
                return True


def check_win_left_diagonal(matrix, player):
    for row in range(len(matrix)-3):
        for column in range(3, len(matrix[row])):
            four_left_diag = [matrix[row][column],
                              matrix[row+1][column-1],
                              matrix[row+2][column-2],
                              matrix[row+3][column-3]]
            if four_left_diag == 4*[player]:
                return True


def check_for_a_tie(matrix):
    if 0 not in matrix[0]:
        print("It's a tie!")
        sleep(2)
        print('You are both either equally good ...')
        sleep(3)
        print('or equally bad!')
        return True


def choose_number_of_rows():
    while True:
        rows = input('Enter the number of playing field rows.\nThe minimum is 5.\n')
        try:
            rows = int(rows)
        except ValueError:
            print('Please use numeric digits.')
            continue

        if rows < 5:
            print('Invalid choice!')
            continue
        else:
            return rows


def choose_number_of_columns():
    while True:
        columns = input('Enter the number of playing field columns.\nThe minimum is 5.\n')
        try:
            columns = int(columns)
        except ValueError:
            print('Please use numeric digits.')
            continue

        if columns < 5:
            print('Invalid choice!')
            continue
        else:
            return columns


def create_matrix():
    rows = choose_number_of_rows()
    columns = choose_number_of_columns()
    the_matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    return the_matrix


def print_the_matrix(matrix):
    print('')
    for row in matrix:
        new_row = '     '
        for el in row:
            if el == 1:
                new_row += '  ' + green + str(el)
            elif el == 2:
                new_row += '  ' + red + str(el)
            else:
                new_row += '  ' + nocolor + str(el)
        print(new_row)
    print(nocolor)


def gameplay_human_vs_human():
    matrix = create_matrix()
    print_the_matrix(matrix)
    players = deque([1, 2])

    while True:
        player = players[0]
        player_move(matrix, player)
        print_the_matrix(matrix)
        if any([check_win_horizontal(matrix, player),
                check_win_vertical(matrix, player),
                check_win_right_diagonal(matrix, player),
                check_win_left_diagonal(matrix, player)]):
            print(f'Player {player} won!')
            break

        elif check_for_a_tie(matrix):
            break

        old_player = players.popleft()
        players.append(old_player)


def gameplay_human_vs_computer():
    matrix = create_matrix()
    print_the_matrix(matrix)

    while True:
        player_move(matrix, 1)
        print_the_matrix(matrix)
        if any([check_win_horizontal(matrix, 1),
                check_win_vertical(matrix, 1),
                check_win_right_diagonal(matrix, 1),
                check_win_left_diagonal(matrix, 1)]):
            print('Player 1 won!')
            break

        if check_for_a_tie(matrix):
            break

        decide_on_action(matrix)
        print_the_matrix(matrix)
        if any([check_win_horizontal(matrix, 2),
                check_win_vertical(matrix, 2),
                check_win_right_diagonal(matrix, 2),
                check_win_left_diagonal(matrix, 2)]):
            print('Player 2 won!')
            break

        if check_for_a_tie(matrix):
            break


def choose_game_mode():
    while True:
        mode = input('Choose game mode:\n'
                     '  1. Human vs Human \n'
                     '  2. Human vs Computer\n')
        try:
            mode = int(mode)
        except ValueError:
            print('Please use numeric digits.')
            continue

        if mode not in [1, 2]:
            print('Invalid choice!')
            continue
        elif mode == 1:
            gameplay_human_vs_human()
            break
        elif mode == 2:
            gameplay_human_vs_computer()
            break



