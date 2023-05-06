def identify_other_player(player):
    if player == 1:
        other_player = 2
    else:
        other_player = 1
    return other_player


# Checks to see if there are elements different from 0 under the 4 elements needed to win horizontally.
def check_foundation_horizontal(matrix, row, column):
    if row == len(matrix)-1:
        return True
    foundation = [matrix[row+1][column+i] for i in range(4)]
    if 0 not in foundation:
        return True


# Checks to see if there are elements different from 0 under the 4 elements needed to win by right diagonal.
def check_foundation_right_diagonal(matrix, row, column):
    if row == len(matrix) - 1:
        foundation = [matrix[row-i][column-1-i] for i in range(3)]
    else:
        foundation = [matrix[row+1-i][column-i] for i in range(4)]

    if 0 not in foundation:
        return True


# Checks to see if there are elements different from 0 under the 4 elements needed to win by right diagonal.
def check_foundation_left_diagonal(matrix, row, column):
    if row == len(matrix)-1:
        foundation = [matrix[row-i][column+1+i] for i in range(3)]
    else:
        foundation = [matrix[row+1-i][column+i] for i in range(4)]

    if 0 not in foundation:
        return True


def first_zero_in_four_elements(list_of_four):
    for i in range(len(list_of_four)):
        if list_of_four[i] == 0:
            return i


def default_next_move(matrix):
    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            return i


def check_moves_horizontal(matrix, player):
    other_player = identify_other_player(player)
    moves_to_win = 5
    sum_of_elements_to_win = 4 * player
    next_move_column = default_next_move(matrix)
    for row in range(len(matrix)-1, -1, -1):
        for column in range(len(matrix[row])-3):
            four_elements = matrix[row][column:column+4]
            if other_player not in four_elements:
                if check_foundation_horizontal(matrix, row, column):
                    sum_of_elements = sum(four_elements)
                    moves = (sum_of_elements_to_win - sum_of_elements)/player
                    if moves_to_win > moves:
                        moves_to_win = moves
                        next_move_column = column + first_zero_in_four_elements(four_elements)
    return moves_to_win, next_move_column


def check_moves_vertical(matrix, player):
    other_player = identify_other_player(player)
    moves_to_win = 5
    sum_of_elements_to_win = 4 * player
    next_move_column = default_next_move(matrix)
    for row in range(len(matrix)-1, 2, -1):
        for column in range(len(matrix[row])):
            four_elements = [matrix[row-i][column] for i in range(4)]
            if other_player not in four_elements:
                sum_of_elements = sum(four_elements)
                moves = (sum_of_elements_to_win - sum_of_elements)/player
                if moves_to_win > moves:
                    moves_to_win = moves
                    next_move_column = column
    return moves_to_win, next_move_column


def check_moves_right_diagonal(matrix, player):
    other_player = identify_other_player(player)
    min_column = 3
    min_row = 3
    moves_to_win = 5
    sum_of_elements_to_win = 4 * player
    next_move_column = default_next_move(matrix)
    for row in range(len(matrix) - 1, -1, -1):
        for column in range(len(matrix[row])):
            if matrix[row][column] != other_player and row >= min_row and column >= min_column:
                if check_foundation_right_diagonal(matrix, row, column):
                    four_elements = [matrix[row][column],
                                     matrix[row-1][column-1],
                                     matrix[row-2][column-2],
                                     matrix[row-3][column-3]]
                    sum_of_elements = sum(four_elements)
                    moves = (sum_of_elements_to_win - sum_of_elements) / player
                    if other_player not in four_elements and moves_to_win > moves:
                        moves_to_win = moves
                        next_move_column = column - first_zero_in_four_elements(four_elements)
    return moves_to_win, next_move_column


def check_moves_left_diagonal(matrix, player):
    other_player = identify_other_player(player)
    min_row = 3
    max_column = len(matrix[0]) - 4
    moves_to_win = 5
    sum_of_elements_to_win = 4 * player
    next_move_column = default_next_move(matrix)
    for row in range(len(matrix) - 1, -1, -1):
        for column in range(len(matrix[row])):
            if matrix[row][column] != other_player and row >= min_row and column <= max_column:
                if check_foundation_left_diagonal(matrix, row, column):
                    four_elements = [matrix[row][column],
                                     matrix[row-1][column+1],
                                     matrix[row-2][column+2],
                                     matrix[row-3][column+3]]
                    sum_of_elements = sum(four_elements)
                    moves = (sum_of_elements_to_win - sum_of_elements) / player
                    if other_player not in four_elements and moves_to_win > moves:
                        moves_to_win = moves
                        next_move_column = column + first_zero_in_four_elements(four_elements)
    return moves_to_win, next_move_column


def next_best_move(matrix, player):
    results_of_checks = [check_moves_horizontal(matrix, player),
                         check_moves_vertical(matrix, player),
                         check_moves_right_diagonal(matrix, player),
                         check_moves_left_diagonal(matrix, player)]
    best_move = 6
    best_column = 0
    for i in range(len(results_of_checks)):
        if results_of_checks[i][0] < best_move:
            best_move = results_of_checks[i][0]
            best_column = results_of_checks[i][1]
    return best_move, best_column


def computer_player_move(matrix, column):
    red = "\033[0;31m"
    for row in range(len(matrix) - 1, -1, -1):
        if matrix[row][column] == 0:
            matrix[row][column] = 2
            print(red + f'Computer player chose column {column+1}')
            break


def decide_on_action(matrix):
    own_move, own_column = next_best_move(matrix, 2)
    enemy_move, enemy_column = next_best_move(matrix, 1)
    if own_move <= enemy_move:
        computer_player_move(matrix, own_column)
    else:
        computer_player_move(matrix, enemy_column)


# check of you are helping enemy with best move




