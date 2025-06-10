def IA_Decision(board, heuristic):
    import random
    return random.choice([c for c in range(12) if board[0][c] == 0])
