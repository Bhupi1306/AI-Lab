## AIM
To design and implement a Tic-Tac-Toe game that uses mathematical logic—based on arithmetic product and magic square sum approaches—to enable the computer to automatically detect winning moves, block opponents, and play optimally.

## THEORY
The objective of both programs is to automate the Tic-Tac-Toe game using logical and mathematical reasoning techniques that enable the computer to identify winning moves, block the opponent, and play optimally. The two implementations achieve this through different mathematical models — one based on arithmetic products and the other on Magic Square sums — yet both rely on analyzing board states efficiently.

1. Board Representation
The Tic-Tac-Toe board is represented as a 1-dimensional vector of size 10 (indices 1–9 used). Each cell holds a numeric value that indicates its state:
    • 2 → Empty cell
    • 3 → Player X’s move
    • 5 → Player O’s move
By using numbers instead of characters, the program can leverage arithmetic operations to determine game outcomes mathematically.

2. Product-Based Game Logic
In the first approach, multiplication patterns are used to detect winning or threatening positions. Each line (row, column, or diagonal) on the board is analyzed by taking the product of its three cell values:
    • X X X = 27 → Player X wins
    • O O O = 125 → Player O wins
    • X X Empty = 18 → X can win next
    • O O Empty = 50 → O can win next
The algorithm checks each row, column, and diagonal. If the product equals 18 or 50, the corresponding empty cell is a winning or blocking move. Otherwise, the program selects the next best available position (center, then sides). This method is efficient because the state of the board can be determined using simple arithmetic comparisons.

3. Magic Square-Based Game Logic
The second approach uses the 3×3 Magic Square concept to detect winning possibilities. In a magic square, every row, column, and diagonal sums to 15. Each board position is mapped to a corresponding magic value. A player wins if the sum of any three of their positions equals 15. For every empty cell, the algorithm checks whether it can complete a line that sums to 15 with two of the player’s existing moves. If yes, that cell is selected as the next move. This approach replaces row/column iteration with mathematical relationships between numbers, resulting in a concise winning strategy.

4. Comparison of Both Methods
Both algorithms follow the same logical flow:
    1. Check if the current player can win.
    2. If not, block the opponent from winning.
    3. If neither condition is true, choose the next best available move.
    4. Update and print the board after every move.
The product-based method relies on multiplicative patterns, while the magic-square method depends on additive relationships. Both perform efficient, constant-time checks and use fixed-size arrays, resulting in similar computational efficiency.

## PROCEDURE
1. Initialize the Tic-Tac-Toe board with all cells set to 2 (empty).
2. Assign Player X as 3 and Player O as 5.
3. On each turn:
   a. Check if the current player can win using Posswin().
   b. If yes, play the winning move.
   c. If not, check if the opponent can win next and block it.
   d. If neither condition is true, select the next best available move (center, corners, or sides).
4. Display the updated board after every move.
5. Continue until all cells are filled or one player wins.

## TIME COMPLEXITY
Each turn involves checking 3 rows, 3 columns, and 2 diagonals, all of which require a fixed number of operations. Thus, the per-turn complexity is constant:
T(n) = O(1)
For 9 moves, the overall complexity remains O(1).


## SPACE COMPLEXITY
Both approaches use a fixed-size board array and a few temporary variables, leading to constant space usage.
Space Complexity: O(1)

## USE CASE
These programs are ideal for demonstrating mathematical reasoning in AI and game development. They are used in educational contexts to teach decision-making logic, heuristic algorithms, and numerical pattern recognition. Additionally, they serve as the basis for AI-based strategy formulation in simple board games.

## CONCLUSION
The Tic-Tac-Toe AI programs successfully automate gameplay using two mathematical techniques — the product-based and magic-square-based approaches. Both provide intelligent move selection through numerical analysis rather than condition-heavy logic, highlighting the power of mathematical abstraction in artificial intelligence. The results demonstrate efficient, optimal gameplay with minimal computation and elegant design.
