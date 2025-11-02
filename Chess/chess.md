## AIM
To implement a simplified chess game where the AI opponent uses the Minimax algorithm enhanced with Alpha-Beta pruning to make intelligent and optimal moves against the human player.
## THEORY
The Minimax algorithm is a decision-making technique used in two-player turn-based games like Chess. It assumes both players play optimally — one tries to maximize their advantage (Maximizer), while the other tries to minimize it (Minimizer). The algorithm explores all possible moves up to a certain depth, evaluates the board states, and chooses the best move based on the evaluation function.
However, due to the huge search space in Chess, the Minimax algorithm can be very slow. To overcome this, Alpha-Beta pruning is used. It eliminates branches that cannot affect the final decision, significantly reducing the number of states explored while still producing the optimal move.
## ALGORITHM USED

1. Initialize the chessboard and set up all pieces in their starting positions.
2. Define an evaluation function that assigns scores to pieces (e.g., +900 for queen, +500 for rook, etc.).
3. For each move, generate all legal moves for the current player.
4. Use the Minimax algorithm to recursively simulate future moves up to a certain depth.
5. Apply Alpha-Beta pruning to skip branches that do not need to be explored:
   - α (alpha) = best already explored option along the path for the maximizer.
   - β (beta) = best already explored option along the path for the minimizer.
6. At each terminal node or depth limit, evaluate the board using the evaluation function.
7. Choose the move that gives the best evaluation score for the AI player.
8. Alternate turns between human and AI until checkmate or a king is captured.

## PROCEDURE

1. Start the program and display the chessboard.
2. Prompt the user to choose a color (White or Black) and AI difficulty (search depth).
3. The player enters moves in standard chess notation (e.g., e2 e4).
4. The AI calculates the best move using the Minimax algorithm with Alpha-Beta pruning up to the specified depth.
5. The board updates after every move, and turns alternate between player and AI.
6. Continue until one of the kings is captured or no legal moves are available (game over).

## TIME COMPLEXITY
Without pruning, the time complexity of Minimax is O(b^d), where:
 - b = branching factor (average number of moves per position, ~35 in chess)
 - d = depth of search

With Alpha-Beta pruning, the average time complexity reduces to O(b^(d/2)) in the best case, allowing the algorithm to search twice as deep in the same amount of time.
## SPACE COMPLEXITY
The space complexity is O(d), where d is the maximum depth of recursion. Each recursive call holds a copy of the board state, so memory usage grows linearly with depth.
USE CASE
This program demonstrates the application of game-tree search algorithms in AI-based games. It can be extended to build stronger chess engines or used as a foundation for developing AIs for other strategic games like Checkers or Connect Four.
## CONCLUSION
The Chess Game using Minimax with Alpha-Beta Pruning demonstrates the power of game-tree search and pruning techniques in artificial intelligence. The AI is capable of analyzing several future moves, pruning unnecessary branches, and making intelligent decisions efficiently. By adjusting the search depth, one can balance between AI strength and computational time.

