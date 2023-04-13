
def create_matrix(rows: int, columns: int):
    the_matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    return the_matrix


def print_the_matrix(matrix):
    for row in matrix:
        print(row)
    print('')


def player_move(matrix, player):
    player_input = int(input(f'Player {player} choose a column:\n'))
    matrix_column = player_input - 1
    for row in range(len(matrix)-1, -1, -1):
        if matrix[row][matrix_column] == 0:
            matrix[row][matrix_column] = player
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
            if matrix[row][column] == player and column > 2 and row <= max_row:
                if matrix[row+1][column-1] == player and matrix[row+2][column-2] == player and matrix[row+3][column-3] == player:
                    return True


def gameplay():
    rows = int(input('Please enter playing field rows:\n'))
    columns = int(input('Please enter playing field columns:\n'))
    matrix = create_matrix(rows, columns)
    print_the_matrix(matrix)

    while True:
        player_move(matrix, 1)
        print_the_matrix(matrix)
        if check_win_horizontal(matrix, 1) or check_win_vertical(matrix, 1) or check_win_right_diagonal(matrix, 1) or check_win_left_diagonal(matrix, 1):
            print('Player 1 won!')
            break

        player_move(matrix, 2)
        print_the_matrix(matrix)
        if check_win_horizontal(matrix, 2) or check_win_vertical(matrix, 2) or check_win_right_diagonal(matrix, 2) or check_win_left_diagonal(matrix, 2):
            print('Player 2 won!')
            break


gameplay()


