# main.py

from game import create_board, print_board, actions, result, Terminal_Test, check_winner
from minimax import IA_Decision
from heuristic import heuristic_func

def switch_player(player):
    return -1 if player == 1 else 1

def play_game(ia_starts=True, ia_vs_ia=False):
    board = create_board()
    player = 1 if ia_starts else -1
    print("Début du jeu !\n")
    print_board(board)

    while not Terminal_Test(board):
        print(f"Tour du joueur {'IA' if player == 1 else 'Humain' if not ia_vs_ia else 'IA2'} :")

        if player == 1 or ia_vs_ia:
            move = IA_Decision(board, heuristic_func)
            print(f"IA joue dans la colonne {move}")
        else:
            valid = False
            while not valid:
                try:
                    move = int(input("Votre coup (colonne 0-11) : "))
                    if move in actions(board):
                        valid = True
                    else:
                        print("Colonne invalide ou pleine.")
                except:
                    print("Entrez un entier valide.")

        board = result(board, move, player)
        print_board(board)
        player = switch_player(player)

    # Résultat final
    if check_winner(board, 1):
        print("Victoire de l’IA !")
    elif check_winner(board, -1):
        print("Victoire du joueur humain !" if not ia_vs_ia else "Victoire de l’IA2 !")
    else:
        print("Match nul.")

if __name__ == "__main__":
    mode = input("Mode de jeu : (1) IA vs Humain, (2) IA vs IA : ")
    if mode == "2":
        play_game(ia_starts=True, ia_vs_ia=True)
    else:
        who_starts = input("Qui commence ? (1) IA, (2) Humain : ")
        play_game(ia_starts=(who_starts == "1"))
