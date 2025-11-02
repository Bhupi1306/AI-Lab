## AIM
To implement a Tic Tac Toe game using the Alpha-Beta Pruning algorithm to optimize the Minimax search process and improve decision-making efficiency.
## THEORY
Alpha-Beta Pruning is an optimization technique for the Minimax algorithm used in two-player turn-based games such as Tic Tac Toe, Chess, and Checkers. It reduces the number of nodes evaluated in the game tree by pruning branches that cannot affect the final decision. The algorithm keeps track of two parameters — Alpha (the best score that the maximizing player can guarantee) and Beta (the best score that the minimizing player can guarantee). When Beta becomes less than or equal to Alpha, the remaining nodes in that branch are pruned as they will not affect the outcome.
## ALGORITHM
1. Start with the current game state and define the players (Computer and Human).
2. Define Alpha as negative infinity and Beta as positive infinity.
3. For each possible move:
   a. Apply the move to the board.
   b. Recursively call the minimax function with the updated Alpha and Beta values.
   c. Undo the move.
4. If the current player is the maximizer (Computer):
   - Update Alpha = max(Alpha, score)
   - Prune the remaining branches if Beta <= Alpha.
5. If the current player is the minimizer (Human):
   - Update Beta = min(Beta, score)
   - Prune the remaining branches if Beta <= Alpha.
6. Return the best possible score for the current player.

## PROCEDURE
1. Initialize the Tic Tac Toe board as a 3x3 grid filled with empty cells.
2. Define functions to check for goal states (win/loss/draw).
3. Implement the Alpha-Beta Pruning version of the Minimax algorithm.
4. Allow the Human player to input their move.
5. Use the bestMove() function to determine the optimal move for the Computer.
6. Continue alternating turns between Human and Computer until a win, loss, or draw occurs.
7. Display the result at the end of the game.

## TIME AND SPACE COMPLEXITY
• Time Complexity: O(b^d) in the worst case, where 'b' is the branching factor and 'd' is the depth of the game tree. 
  However, Alpha-Beta Pruning can reduce the effective branching factor, making it closer to O(b^(d/2)) in the best case.
• Space Complexity: O(b * d) due to the recursive call stack and board storage.

## USE CASE
Alpha-Beta Pruning is widely used in artificial intelligence for decision-making in adversarial games like Chess, Checkers, Tic Tac Toe, and Connect Four. 
It is especially useful when the search space is large, and we need an optimized way to find the best move without exploring all possibilities.
## CONCLUSION
The implementation of Tic Tac Toe using Alpha-Beta Pruning demonstrates how search tree optimization can significantly reduce computational time 
while maintaining optimal decision-making. The algorithm effectively prunes unneeded branches, making it faster than the basic Minimax approach.

