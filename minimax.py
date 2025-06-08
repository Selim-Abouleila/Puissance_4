# minimax.py
import math
from game import actions, result, Terminal_Test, check_winner

MAX_DEPTH = 4  # Vous pouvez ajuster selon les performances

def utility(board):
    """Évaluation simple du résultat final."""
    if check_winner(board, 1):     # IA gagne
        return 1000
    elif check_winner(board, -1):  # Adversaire gagne
        return -1000
    else:
        return 0  # Match nul

def minimax(board, depth, alpha, beta, maximizing_player, heuristic_func):
    if Terminal_Test(board) or depth == 0:
        return heuristic_func(board), None

    best_action = None
    if maximizing_player:
        value = -math.inf
        for action in actions(board):
            child = result(board, action, 1)
            eval_score, _ = minimax(child, depth - 1, alpha, beta, False, heuristic_func)
            if eval_score > value:
                value = eval_score
                best_action = action
            alpha = max(alpha, value)
            if alpha >= beta:
                break  # Élagage Beta
    else:
        value = math.inf
        for action in actions(board):
            child = result(board, action, -1)
            eval_score, _ = minimax(child, depth - 1, alpha, beta, True, heuristic_func)
            if eval_score < value:
                value = eval_score
                best_action = action
            beta = min(beta, value)
            if beta <= alpha:
                break  # Élagage Alpha
    return value, best_action

def IA_Decision(board, heuristic_func):
    """
    Appel principal pour que l'IA choisisse un coup. Elle joue en tant que joueur 1.
    """
    _, action = minimax(board, MAX_DEPTH, -math.inf, math.inf, True, heuristic_func)
    return action
