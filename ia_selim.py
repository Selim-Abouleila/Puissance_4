# ia_selim.py

import random
from game import actions

def IA_Decision(board, heuristic):
    """
    IA très simple : joue aléatoirement parmi les colonnes valides,
    sauf si une colonne centrale est dispo (elle est priorisée).
    """
    valid_moves = actions(board)

    # S'il peut jouer au centre, il préfère
    for col in [5, 6]:
        if col in valid_moves:
            return col

    # Sinon il joue aléatoirement
    return random.choice(valid_moves)
