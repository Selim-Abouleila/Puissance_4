# heuristic.py

ROWS = 6
COLS = 12

def heuristic_func(board):
    """
    Évalue un état non terminal : +score si IA (1) est bien placée, -score si adversaire (-1) l'est.
    """
    score = 0

    # Analyse chaque ligne, colonne et diagonale
    directions = [
        (0, 1),  # Horizontal →
        (1, 0),  # Vertical ↓
        (1, 1),  # Diagonal ↘
        (1, -1)  # Diagonal ↙
    ]

    for row in range(ROWS):
        for col in range(COLS):
            for dx, dy in directions:
                score += evaluate_line(board, row, col, dx, dy)

    return score

def evaluate_line(board, row, col, dx, dy):
    """
    Évalue une séquence de 4 cases à partir de (row, col) dans la direction (dx, dy).
    Retourne un score en fonction du nombre de pions 1 (IA) ou -1 (adversaire).
    """
    line = []
    for i in range(4):
        r = row + i * dx
        c = col + i * dy
        if 0 <= r < ROWS and 0 <= c < COLS:
            line.append(board[r][c])
        else:
            return 0  # Hors grille

    return score_line(line)

def score_line(line):
    """
    Donne un score à une ligne de 4 cases.
    """
    if line.count(1) > 0 and line.count(-1) == 0:
        return [0, 1, 10, 100, 1000][line.count(1)]
    elif line.count(-1) > 0 and line.count(1) == 0:
        return -[0, 1, 10, 100, 1000][line.count(-1)]
    return 0
