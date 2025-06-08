# Puissance 4 – Minimax AI Battle

This project implements an AI for a Connect Four (Puissance 4) game using the Minimax algorithm with Alpha-Beta pruning. It allows human vs AI or AI vs AI games with a customizable heuristic and limited depth to ensure fast decision-making.

## AI Approach

- Minimax with Alpha-Beta Pruning: Reduces the search tree size.
- Heuristic Evaluation: Scores board states based on potential alignments of 2, 3, or 4 pieces.
- Depth Limiting: Controls computation time per move (default = 4).

## File Structure

- game.py — Game logic: board creation, moves, win detection.
- minimax.py — Minimax + Alpha-Beta pruning + decision function.
- heuristic.py — Heuristic scoring for non-terminal board states.
- main.py — Runs the game (IA vs IA or Human vs IA).

## How to Play

Run the main script in terminal:

--bash
python main.py

You'll be asked to choose:
-IA vs Human
-IA vs IA
--Who starts the game



. = Empty cell
