from computer_player import *

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
    max_column = len(matrix[0]) - 4
    for row in matrix:
        for column in range(len(row)):
            if row[column] == player and column <= max_column:
                if row[column+1] == player and row[column+2] == player and row[column+3] == player:
                    return True


def check_win_vertical(matrix, player):
    max_row = len(matrix) - 4
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == player and row <= max_row:
                if matrix[row+1][column] == player and matrix[row+2][column] == player and matrix[row+3][column] == player:
                    return True


def check_win_right_diagonal(matrix, player):
    max_column = len(matrix[0]) - 4
    max_row = len(matrix) - 4
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == player and column <= max_column and row <= max_row:
                if matrix[row+1][column+1] == player and matrix[row+2][column+2] == player and matrix[row+3][column+3] == player:
                    return True


def check_win_left_diagonal(matrix, player):
    max_row = len(matrix) - 4
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == player and column >= 3 and row <= max_row:
                if matrix[row+1][column-1] == player and matrix[row+2][column-2] == player and matrix[row+3][column-3] == player:
                    return True


def choose_number_of_rows():
    while True:
        rows = input('Please enter playing field rows.\nThe minimum is 5.\n')
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
        columns = input('Please enter playing field columns.\nThe minimum is 5.\n')
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

    while True:
        player_move(matrix, 1)
        print_the_matrix(matrix)
        if any([check_win_horizontal(matrix, 1),
                check_win_vertical(matrix, 1),
                check_win_right_diagonal(matrix, 1),
                check_win_left_diagonal(matrix, 1)]):
            print('Player 1 won!')
            break

        player_move(matrix, 2)
        print_the_matrix(matrix)
        if any([check_win_horizontal(matrix, 2),
                check_win_vertical(matrix, 2),
                check_win_right_diagonal(matrix, 2),
                check_win_left_diagonal(matrix, 2)]):
            print('Player 2 won!')
            break

        if 0 not in matrix[0]:
            print("It's a tie! You both either equally good or equally bad!")
            break


def gameplay_human_vs_computer():
    matrix = create_matrix()
    print_the_matrix(matrix)

    while True:
        player_move(matrix, 1)
        print_the_matrix(matrix)
        if any([check_win_horizontal(matrix, 1),
                check_win_vertical(matrix, 1),
                check_win_right_diagonal(matrix,1),
                check_win_left_diagonal(matrix, 1)]):
            print('Player 1 won!')
            break

        decide_on_action(matrix)
        print_the_matrix(matrix)
        if any([check_win_horizontal(matrix, 2),
                check_win_vertical(matrix, 2),
                check_win_right_diagonal(matrix, 2),
                check_win_left_diagonal(matrix, 2)]):
            print('Player 2 won!')
            break

        if 0 not in matrix[0]:
            print("It's a tie! You both either equally good or equally bad!")
            break


def choose_game_mode():
    while True:
        mode = input('Choose game mode:\n  1. Human vs Human \n  2. Human vs Computer\n')
        try:
            mode = int(mode)
        except ValueError:
            print('Please use numeric digits.')
            continue

        if mode not in [1,2]:
            print('Invalid choice!')
            continue
        elif mode == 1:
            gameplay_human_vs_human()
            break
        elif mode == 2:
            gameplay_human_vs_computer()
            break
