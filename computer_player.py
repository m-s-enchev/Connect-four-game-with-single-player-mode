def identify_other_player(player):
    if player == 1:
        other_player = 2
    else:
        other_player = 1
    return other_player


class CheckFoundation:
    """Checks to see if there are elements different from 0 under the 4 elements needed to win"""
    def __init__(self, matrix, row, column):
        self.matrix = matrix
        self.row = row
        self.column = column
        self.bottom = len(matrix)-1

    def horizontal(self):
        if self.row == self.bottom:
            return True
        foundation = [self.matrix[self.row+1][self.column+i] for i in range(4)]

        if 0 not in foundation:
            return True

    def right_diagonal(self):
        if self.row == self.bottom:
            foundation = [self.matrix[self.row-i][self.column-1-i] for i in range(3)]
        else:
            foundation = [self.matrix[self.row+1-i][self.column-i] for i in range(4)]

        if 0 not in foundation:
            return True

    def left_diagonal(self):
        if self.row == self.bottom:
            foundation = [self.matrix[self.row-i][self.column+1+i] for i in range(3)]
        else:
            foundation = [self.matrix[self.row+1-i][self.column+i] for i in range(4)]

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


class CheckMovesToWin:
    MOVES_TO_WIN = 5

    def __init__(self, matrix, player):
        self.player = player
        self.matrix = matrix
        self.other_player = identify_other_player(self.player)
        self.sum_of_elements_to_win = 4 * self.player
        self.next_move_column = default_next_move(matrix)

    def horizontal(self):
        for row in range(len(self.matrix)-1, -1, -1):
            for column in range(len(self.matrix[row])-3):
                four_elements = self.matrix[row][column:column+4]
                if CheckFoundation(self.matrix, row, column).horizontal():
                    if self.other_player not in four_elements:
                        sum_of_elements = sum(four_elements)
                        moves = (self.sum_of_elements_to_win - sum_of_elements)/self.player
                        if self.MOVES_TO_WIN > moves:
                            self.MOVES_TO_WIN = moves
                            self.next_move_column = column + first_zero_in_four_elements(four_elements)

    def vertical(self):
        for row in range(len(self.matrix)-1, 2, -1):
            for column in range(len(self.matrix[row])):
                four_elements = [self.matrix[row-i][column] for i in range(4)]
                if self.other_player not in four_elements:
                    sum_of_elements = sum(four_elements)
                    moves = (self.sum_of_elements_to_win - sum_of_elements)/self.player
                    if self.MOVES_TO_WIN > moves:
                        self.MOVES_TO_WIN = moves
                        self.next_move_column = column

    def right_diagonal(self):
        for row in range(len(self.matrix) - 1, 2, -1):
            for column in range(3, len(self.matrix[row])):
                four_elements = [self.matrix[row-i][column-i] for i in range(4)]
                if CheckFoundation(self.matrix, row, column).right_diagonal():
                    if self.other_player not in four_elements:
                        sum_of_elements = sum(four_elements)
                        moves = (self.sum_of_elements_to_win - sum_of_elements) / self.player
                        if self.MOVES_TO_WIN > moves:
                            self.MOVES_TO_WIN = moves
                            self.next_move_column = column - first_zero_in_four_elements(four_elements)

    def left_diagonal(self):
        for row in range(len(self.matrix) - 1, 2, -1):
            for column in range(len(self.matrix[row])-3):
                four_elements = [self.matrix[row-i][column+i] for i in range(4)]
                if CheckFoundation(self.matrix, row, column).left_diagonal():
                    if self.other_player not in four_elements:
                        sum_of_elements = sum(four_elements)
                        moves = (self.sum_of_elements_to_win - sum_of_elements) / self.player
                        if self.MOVES_TO_WIN > moves:
                            self.MOVES_TO_WIN = moves
                            self.next_move_column = column + first_zero_in_four_elements(four_elements)

    def best_next_move(self):
        self.horizontal()
        self.vertical()
        self.right_diagonal()
        self.left_diagonal()
        return self.MOVES_TO_WIN, self.next_move_column


def computer_player_move(matrix, column):
    red = "\033[0;31m"
    for row in range(len(matrix) - 1, -1, -1):
        if matrix[row][column] == 0:
            matrix[row][column] = 2
            print(red + f'Computer player chose column {column+1}')
            break


def decide_on_action(matrix):
    own_move, own_column = CheckMovesToWin(matrix, 2).best_next_move()
    enemy_move, enemy_column = CheckMovesToWin(matrix, 1).best_next_move()
    if own_move <= enemy_move:
        computer_player_move(matrix, own_column)
    else:
        computer_player_move(matrix, enemy_column)


# check of you are helping enemy with best move




