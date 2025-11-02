# Tic Tac Toe with Minimax Algorithm

## Overview
This project implements the classic Tic Tac Toe game where the computer opponent uses the Minimax Algorithm to make optimal decisions.  
The AI always plays optimally, making it impossible for a human player to win if the algorithm is used correctly.  

## Theory

### What is Minimax?
- Minimax is a backtracking algorithm used in decision-making and game theory.  
- It provides an optimal move for the player assuming the opponent also plays optimally.  
- The algorithm simulates all possible moves, recursively evaluates them, and selects the move that maximizes the player’s chance of winning while minimizing the opponent’s.

### Working Principle
1. Maximizer (AI) tries to maximize the score.
2. Minimizer (Human) tries to minimize the score.
3. The algorithm explores all possible future states of the game using recursion.
4. The score is assigned as:
   - +10 → AI win  
   - -10 → Human win  
   - 0 → Draw  

## Algorithm (Pseudocode)

if isMaximizing:
    bestScore = -∞
    for each possible move:
        make move
        score = minimax(board, depth + 1, false)
        undo move
        bestScore = max(bestScore, score)
    return bestScore
else:
    bestScore = +∞
    for each possible move:
        make move
        score = minimax(board, depth + 1, true)
        undo move
        bestScore = min(bestScore, score)
    return bestScore


## Time Complexity

- Worst Case:  
  Tic Tac Toe has at most 9 moves.  
  The Minimax algorithm explores the full game tree:  
  O(b^d) = O(9!) ≈ O(362,880)  
  where:
  - b = branching factor (number of available moves)
  - d = depth (max number of moves in a game)

- With pruning (Alpha-Beta Pruning), this can be reduced significantly.  
- In practice, Tic Tac Toe’s small state space makes Minimax feasible without pruning.

## Space Complexity
- Each recursive call stores the game state.  
- Maximum recursion depth = 9 (total moves).  
- Space Complexity: O(d) = O(9) → effectively O(1).

## Features
- Human vs AI gameplay.
- AI always plays optimally using Minimax.
- Supports detection of win, loss, and draw states.
- Simple and modular implementation.

## Example Game Flow
1. Human plays first as X.
2. AI (using Minimax) plays optimally as O.
3. The game continues until a win or draw is detected.

## Conclusion
- The Minimax Algorithm guarantees the best possible move for the AI.  
- In Tic Tac Toe, this means the AI can never lose.  
- Demonstrates concepts of recursion, backtracking, and game theory.  
- This project can be extended to more complex games (like Connect Four, Chess, etc.) with optimizations such as Alpha-Beta Pruning.



