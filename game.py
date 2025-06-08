ROWS = 6
COLS = 12

def create_board():
    return [[0 for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    for row in board:
        print(' '.join(str(cell) if cell != 0 else '.' for cell in row))
    print(" ".join(map(str, range(COLS))))

def actions(board):
    return [col for col in range(COLS) if board[0][col] == 0]

def result(board, action, player):
    from copy import deepcopy
    new_board = deepcopy(board)
    for row in reversed(range(ROWS)):
        if new_board[row][action] == 0:
            new_board[row][action] = player
            break
    return new_board

def check_winner(board, player):
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True
    for row in range(ROWS - 3):
        for col in range(COLS):
            if all(board[row + i][col] == player for i in range(4)):
                return True
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True
    return False

def Terminal_Test(board):
    return check_winner(board, 1) or check_winner(board, -1) or all(board[0][c] != 0 for c in range(COLS))
