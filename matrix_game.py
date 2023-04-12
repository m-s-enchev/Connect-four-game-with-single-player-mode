

the_matrix = [[0 for _ in range(7)] for _ in range(6)]


def print_the_matrix():
    for x in the_matrix:
        print(x)


def player_one_move():
    player_input = int(input())
    matrix_column = player_input - 1
    for i in range(len(the_matrix)-1, -1, -1):
        if the_matrix[i][matrix_column] == 0:
            the_matrix[i][matrix_column] = 1
            break


def player_two_move():
    player_input = int(input())
    matrix_column = player_input - 1
    for i in range(len(the_matrix)-1, -1, -1):
        if the_matrix[i][matrix_column] == 0:
            the_matrix[i][matrix_column] = 2
            break

            
def check_win_horizontal(player):
    for y in the_matrix:
        for x in range(len(y)):
            if y[x] == player and x < 4:
                if y[x+1] == player and y[x+2] == player and y[x+3] == player:
                    return True


def check_win_vertical(player):
    for y in range(len(the_matrix)):
        for x in range(len(the_matrix[y])):
            if the_matrix[y][x] == player and y < 3:
                if the_matrix[y+1][x] == player and the_matrix[y+2][x] == player and the_matrix[y+3][x] == player:
                    return True

def check_win_right_diagonal(player):
    for y in range(len(the_matrix)):
        for x in range(len(the_matrix[y])):
            if the_matrix[y][x] == player and x < 4 and y < 3:
                if the_matrix[y+1][x+1] == player and the_matrix[y+2][x+2] == player and the_matrix[y+3][x+3] == player:
                    return True

def check_win_left_diagonal(player):
    for y in range(len(the_matrix)):
        for x in range(len(the_matrix[y])):
            if the_matrix[y][x] == player and x > 2 and y < 3:
                if the_matrix[y+1][x-1] == player and the_matrix[y+2][x-2] == player and the_matrix[y+3][x-3] == player:
                    return True


while True:
    player_one_move()
    print_the_matrix()
    if check_win_horizontal(1) or check_win_vertical(1) or check_win_right_diagonal(1) or check_win_left_diagonal(1):
        print('Player 1 won!')
        break

    player_two_move()
    print_the_matrix()
    if check_win_horizontal(2) or check_win_vertical(2) or check_win_right_diagonal(2) or check_win_left_diagonal(2):
        print('Player 2 won!')
        break


