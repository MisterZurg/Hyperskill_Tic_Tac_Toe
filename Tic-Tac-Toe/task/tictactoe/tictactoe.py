# write your code here
# Stage 1/5 Welcome to the battlefield!
def print_аny_field():
    print(f"X O X\n" \
          "O X O\n" \
          "X X O")


# Stage 2/5 The user is the gamemaster
# Отображаем списка 3 элемента на новой строке
def print_field_simple(sequence):
    print("---------")
    for i in range(0, len(sequence), 3):
        print("|", *sequence[i:i + 3], "|", sep=" ")
    print("---------")


# Рассматриваем все 8 случаев:
# - x3
# | x3
# \ x1
# / x1
def get_lines_cools_diagonals(sequence):
    combinatioms = []
    combinatioms.append(sequence[0] + sequence[1] + sequence[2])
    combinatioms.append(sequence[3] + sequence[4] + sequence[5])
    combinatioms.append(sequence[6] + sequence[7] + sequence[8])
    combinatioms.append(sequence[0] + sequence[4] + sequence[8])
    combinatioms.append(sequence[2] + sequence[4] + sequence[6])
    combinatioms.append(sequence[0] + sequence[3] + sequence[6])
    combinatioms.append(sequence[1] + sequence[4] + sequence[7])
    combinatioms.append(sequence[2] + sequence[5] + sequence[8])
    return combinatioms


def enter_move(sequence):
    # Cells are entered in a list with positions 0 - 8
    # and are mapped to a grid like this:
    # 0 1 2
    # 3 4 5
    # 6 7 8

    # The new grid is:
    # (1, 3) (2, 3) (3, 3)
    # (1, 2) (2, 2) (3, 2)
    # (1, 1) (2, 1) (3, 1)
    users_data = [x for x in input('Enter the coordinates: ').split()]
    # col, row = input('Enter the coordinates: ').split()
    while not is_valid(users_data):
        # col, row = input('Enter the coordinates: ').split()
        users_data = [x for x in input('Enter the coordinates: ').split()]

    # Stage 4/5 First move!  (formula convert coords into index)
    col = int(users_data[0]) - 1
    row = 3 - int(users_data[1])
    index = (row * 3) + col

    # Проверка на пустоту is_empty
    can_print = False
    if not is_empty(sequence, index):
        can_print = False
        enter_move(sequence)
    else:
        can_print = True
    if can_print:
        print_field_simple(sequence)


def is_valid(users_data):
    if len(users_data) == 2:
        col, row = users_data[0], users_data[1]
        if col.isdigit() and row.isdigit():
            if 1 <= int(col) <= 3 and 1 <= int(row) <= 3:
                return True
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")
    else:
        # Будем считать что он ввел только одно слово :/
        print("You should enter numbers!")


def is_empty(seq, index):
    if seq[index] == '_':
        seq[index] = 'X'
        return True
    else:
        print("This cell is occupied! Choose another one!")


# Stage 3/5: What's up on the field?
def decide_winner(seq):
    uderscore_count = seq.count('_')
    x_count = seq.count('X')
    o_count = seq.count('O')
    # Impossible
    if ((x_count + 1 < o_count) or
        (o_count + 1 < x_count)) or (
            'XXX' in get_lines_cools_diagonals(seq) and 'OOO' in get_lines_cools_diagonals(seq)):
        print('Impossible')
    # Game not finished
    elif 'XXX' not in get_lines_cools_diagonals(seq) and 'OOO' not in get_lines_cools_diagonals(seq) \
            and uderscore_count != 0:  # any("_" in t for t in get_lines_cools_diagonals(seq)):
        print('Game not finished')
    # Draw
    elif 'XXX' not in get_lines_cools_diagonals(seq) and 'OOO' not in get_lines_cools_diagonals(seq) \
            and uderscore_count == 0:
        print('Draw')
    # X wins
    elif 'XXX' in get_lines_cools_diagonals(seq):
        print('X wins')
    # O wins
    elif 'OOO' in get_lines_cools_diagonals(seq):
        print('O wins')
    else:
        print('Impossible')


# Stage 3/5: What's up on the field? appendix
# sequence = list(input("Enter cells: "))
# print_field_simple(sequence)

# Stage 5/5 Fight!
# Собственно Tic-Tac-Toe
# Переход от листа: [],
# ко вложенным листам: [[],[],[]]
def print_field(matrix):
    print("--------")
    for i in range(3):
        print("|", matrix[i][0], matrix[i][1], matrix[i][2], "|")
    print("--------")


def check_row(matrix):
    new_list = []
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2]:
            if matrix[i][0] != '_':
                new_list.append(matrix[0][i])
    return new_list


def check_column(matrix):
    new_list = []
    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i]:
            if matrix[0][i] != '_':
                new_list.append(matrix[0][i])
    return new_list


def check_diagonal(matrix):
    new_list = []
    if matrix[0][0] == matrix[1][1] == matrix[2][2] or matrix[2][0] == matrix[1][1] == matrix[0][2]:
        if matrix[1][1] != '_':
            new_list.append(matrix[1][1])
    return new_list


def check_draw(matrix):
    return all([matrix[n][i] != '_' for n in range(3) for i in range(3)])


def winner(matrix):
    return check_column(matrix) + check_row(matrix) + check_diagonal(matrix)


# Cells are entered in a list with positions 0 - 8
# and are mapped to a grid like this:
# 0 1 2
# 3 4 5
# 6 7 8

# The new grid is:
# (1, 3) (2, 3) (3, 3)
# (1, 2) (2, 2) (3, 2)
# (1, 1) (2, 1) (3, 1)

# turn odd — 'X'
# turn even — 'O'


def player_turn():
    while True:
        coords = input('Enter the coordinates: ')
        y, x = coords.split()
        if not (x.isdigit() and y.isdigit()):
            print('You should enter numbers!')
            continue
        if int(x) not in range(1, 4) or int(y) not in range(1, 4):
            print('Coordinates should be from 1 to 3!')
            continue
        y = int(y) - 1
        x = 3 - int(x)
        if t_t_t[x][y] == '_':
            global turn
            turn += 1
            if turn % 2:
                t_t_t[x][y] = 'X'
            else:
                t_t_t[x][y] = 'O'
            print_field(t_t_t)
            break
        else:
            print('This cell is occupied! Choose another one!')


tic_tac_toe = list('_' * 9)
turn = 0  # For turn order, who plays 'X' or 'O'
t_t_t = [[tic_tac_toe[0 + i * 3], tic_tac_toe[1 + i * 3], tic_tac_toe[2 + i * 3]] for i in range(3)]
# a.k.a.
# t_t_t = [[tic_tac_toe[0], tic_tac_toe[1], tic_tac_toe[2]],
#          [tic_tac_toe[3], tic_tac_toe[4], tic_tac_toe[5]],
#          [tic_tac_toe[6], tic_tac_toe[7], tic_tac_toe[8]]]

print_field(t_t_t)

while all([not winner(t_t_t), not check_draw(t_t_t)]):
    player_turn()
else:
    print(f'{winner(t_t_t)[0]} wins' if winner(t_t_t) else 'Draw')
