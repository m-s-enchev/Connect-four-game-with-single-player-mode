def identify_other_player(player):
    if player == 1:
        other_player = 2
    else:
        other_player = 1
    return other_player


# Checks to see if there are elements different from 0 under the 3 elements needed to win horizontally.
def check_foundation_horizontal(matrix, row, column):
    if row == len(matrix)-1:
        return True
    foundation = [matrix[row-1][column+1], matrix[row-1][column+2], matrix[row-1][column+3]]
    if 0 not in foundation:
        return True


def check_moves_horizontal(matrix, player):
    other_player = identify_other_player(player)
    max_column = len(matrix[0]) - 4
    moves_to_win = 4
    sum_of_elements_to_win = 3 * player
    next_move_column = None
    for row in range(len(matrix)-1, -1, -1):
        for column in range(len(matrix[row])):
            if matrix[row][column] == player and column <= max_column:
                if check_foundation_horizontal(matrix, row, column):
                    three_consecutive_positions = [matrix[row][column+1], matrix[row][column+2], matrix[row][column+3]]
                    sum_of_elements = sum(three_consecutive_positions)
                    moves = (sum_of_elements_to_win - sum_of_elements)/player
                    if other_player not in three_consecutive_positions and moves_to_win > moves:
                        moves_to_win = moves
                        next_move_column = column
    return moves_to_win, next_move_column



def check_moves_vertical(matrix, player):
    other_player = identify_other_player(player)
    min_row = 3
    moves_to_win = 4
    sum_of_elements_to_win = 3 * player
    next_move_column = None
    for row in range(len(matrix)-1, -1, -1):
        for column in range(len(matrix[row])):
            if matrix[row][column] == player and row >= min_row:
                three_consecutive_positions = [matrix[row-1][column], matrix[row-2][column], matrix[row-3][column]]
                sum_of_elements = sum(three_consecutive_positions)
                moves = (sum_of_elements_to_win - sum_of_elements)/player
                if other_player not in three_consecutive_positions and moves_to_win > moves:
                    moves_to_win = moves
                    next_move_column = column
    return moves_to_win, next_move_column


# Checks to see if there are elements different from 0 under the 3 elements needed to win by right diagonal.
def check_foundation_right_diagonal(matrix, row, column):
    foundation = [matrix[row][column-1], matrix[row-1][column-2], matrix[row-2][column-3]]
    if 0 not in foundation:
        return True


def check_moves_right_diagonal(matrix, player):
    other_player = identify_other_player(player)
    min_column = 3
    min_row = 3
    moves_to_win = 4
    sum_of_elements_to_win = 3 * player
    next_move_column = None
    for row in range(len(matrix) - 1, -1, -1):
        for column in range(len(matrix[row])):
            if matrix[row][column] == player and row >= min_row and column >= min_column:
                if check_foundation_right_diagonal(matrix, row, column):
                    three_consecutive_positions = [matrix[row-1][column-1], matrix[row-2][column-2], matrix[row-3][column-3]]
                    sum_of_elements = sum(three_consecutive_positions)
                    moves = (sum_of_elements_to_win - sum_of_elements) / player
                    if other_player not in three_consecutive_positions and moves_to_win > moves:
                        moves_to_win = moves
                        next_move_column = column
    return moves_to_win, next_move_column


# Checks to see if there are elements different from 0 under the 3 elements needed to win by right diagonal.
def check_foundation_left_diagonal(matrix, row, column):
    foundation = [matrix[row][column-1], matrix[row-1][column-2], matrix[row-2][column-3]]
    if 0 not in foundation:
        return True


def check_moves_left_diagonal(matrix, player):
    other_player = identify_other_player(player)
    min_row = 3
    max_column = len(matrix[0]) - 4
    moves_to_win = 4
    sum_of_elements_to_win = 3 * player
    next_move_column = None
    for row in range(len(matrix) - 1, -1, -1):
        for column in range(len(matrix[row])):
            if matrix[row][column] == player and row >= min_row and column <= max_column:
                if check_foundation_left_diagonal(matrix, row, column):
                    three_consecutive_positions = [matrix[row-1][column+1], matrix[row-2][column+2], matrix[row-3][column+3]]
                    sum_of_elements = sum(three_consecutive_positions)
                    moves = (sum_of_elements_to_win - sum_of_elements) / player
                    if other_player not in three_consecutive_positions and moves_to_win > moves:
                        moves_to_win = moves
                        next_move_column = column
    return moves_to_win, next_move_column


def next_best_move(matrix, player):
    moves_h, column_h = check_moves_horizontal(matrix, player)
    moves_v, column_v = check_moves_vertical(matrix, player)
    moves_r, column_r = check_moves_right_diagonal(matrix, player)
    moves_l, column_l = check_moves_left_diagonal(matrix, player)
    results_of_checks = {moves_h: column_h, moves_v: column_v, moves_r: column_r, moves_l: column_l}
    best_move = min(results_of_checks)
    return results_of_checks[best_move]







