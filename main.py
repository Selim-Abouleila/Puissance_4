from game import create_board, print_board, actions, result, Terminal_Test, check_winner
from minimax import IA_Decision as my_ia
from heuristic import heuristic_func
import importlib

def switch_player(player):
    return -1 if player == 1 else 1

def load_opponent_ia(module_name):
    try:
        module = importlib.import_module(module_name)
        return module.IA_Decision
    except Exception as e:
        print(f"Erreur de chargement de l'IA adverse '{module_name}': {e}")
        print("IA adverse jouera aléatoirement.")
        import random
        return lambda board, heuristic: random.choice(actions(board))

def play_game(opponent_ia_func, mode="IA_VS_IA", ia_starts=True):
    board = create_board()
    player = 1 if ia_starts else -1
    print_board(board)

    while not Terminal_Test(board):
        if mode == "IA_VS_HUMAN":
            if player == 1:
                move = my_ia(board, heuristic_func)
            else:
                valid = False
                while True:
                    try:
                        move = int(input("Entrez une colonne (0–11) : "))
                        if move in actions(board):
                            break
                        else:
                            print("Colonne invalide.")
                    except:
                        print("Erreur de saisie.")
        else:
            move = my_ia(board, heuristic_func) if player == 1 else opponent_ia_func(board, heuristic_func)

        print(f"Colonne choisie : {move}")
        board = result(board, move, player)
        print_board(board)
        player = switch_player(player)

    if check_winner(board, 1):
        print("Votre IA a gagné !")
    elif check_winner(board, -1):
        print("L’IA adverse a gagné !")
    else:
        print("Match nul.")

if __name__ == "__main__":
    print("Modes disponibles :\n1 - IA vs IA externe\n2 - IA vs Humain")
    choix = input("Choisissez un mode (1 ou 2) : ")

    if choix == "1":
        nom_module = input("Nom du fichier Python de l’IA adverse (sans .py) : ")
        opponent_ia_func = load_opponent_ia(nom_module)
        play_game(opponent_ia_func, mode="IA_VS_IA")
    else:
        play_game(None, mode="IA_VS_HUMAN")
