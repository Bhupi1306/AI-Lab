# Best First Search for 8-Puzzle Problem
Problem Statement

The 8-puzzle problem is a sliding puzzle that consists of a 3×3 board with tiles numbered from 1 to 8 and a blank space (0).

## Algorithm (Best-First Search)
1. Insert the initial state (root) into a priority queue.
2. Define a heuristic function h(n) to evaluate how close each state is to the goal.
3. Repeatedly pick the state with the lowest heuristic value from the priority queue.
4. If this state is the goal state, stop and return success.
5. Otherwise, generate all possible child states (by moving the blank tile up, down, left, or right).
6. If a child state has not been visited before, insert it into the priority queue.
7. Continue until the queue is empty (failure) or goal is found.

## Misplaced Tiles Heuristic
• Counts the number of tiles that are not in their correct position compared to the goal state.
• Example:
Current:   1 2 3       Goal:   1 2 3
           4 6 5              4 5 6
           7 8 0              7 8 0

Here, 2 tiles (5 and 6) are misplaced → h(n) = 2.

• Formula:
    h(n) = sum( node[i][j] != goal[i][j] for all i,j )

• Advantages:
  - Very fast to compute.
• Disadvantages:
  - Not very accurate, as it ignores the actual distance of misplaced tiles.
## Manhattan Distance Heuristic
• Measures the sum of the row and column distances each tile is away from its goal position.
• Example:
Current:   1 2 3       Goal:   1 2 3
           4 6 5               4 5 6
           7 8 0               7 8 0

Tile 5 is at (1,2) instead of (1,1) → distance = 1.
Tile 6 is at (1,1) instead of (1,2) → distance = 1.
Total Manhattan distance = 2.

### Formula:
    h(n) = sum( |x_current - x_goal| + |y_current - y_goal| for all tiles )

### Advantages:
  - More accurate than misplaced tiles.
  - Admissible and consistent heuristic → guarantees optimal solution with A*.
### Disadvantages:
  - Slower to compute than misplaced tiles.

## Theory
Best-First Search uses a heuristic to expand the 'most promising' node first.
In the 8-puzzle, the heuristic estimates how close we are to the solution.
Different heuristics can drastically change the performance of the algorithm:
  - Misplaced Tiles: quick but less accurate.
  - Manhattan Distance: slower but much more accurate.
Time Complexity
In the worst case, Best-First Search explores a large portion of the state space.
For the 8-puzzle, the maximum number of states = 9! = 362,880.

## Time complexity depends on the heuristic:
  - Misplaced Tiles: explores more states (weaker heuristic).
  - Manhattan Distance: explores fewer states (stronger heuristic).

Average Time Complexity:
    O(b^d)
where b = branching factor (≈ 4) and d = depth of solution.


# Tic Tac Toe

Tic Tac Toe is a two-player game played on a 3×3 grid. Players alternate marking X or O until one wins or the board is full.

Winning condition: Three identical symbols in a row, column, or diagonal.
AI Strategies used in this program:
1. Check Win – If a winning move is available, take it.
2. Block Opponent – If the opponent can win next move, block it.
3. Take Center – Prefer center if available.
4. Take Corners/Edges – Otherwise take strategic positions.

This program uses multiplicative encoding:
    X = 3, O = 5, Blank = 2
    If the product of a row/col/diagonal is 18 (3×3×2), then X can win.
    If product = 50 (5×5×2), then O can win.

## Second version
This program implements Tic Tac Toe using the magic square method, where each cell of the 3×3 board is mapped to numbers in a magic square such that any winning row, column, or diagonal always sums to 15. 
The board is represented with values 2 (empty), 3 (X), and 5 (O), and the Posswin function checks if a player can win by verifying whether two of their chosen numbers along with an empty cell’s magic number add up to 15. 
The strategy first plays the center if available, otherwise a corner, then on each turn it either takes a winning move, blocks the opponent, or chooses the next free cell. 
This avoids brute-force row/column checks, making the algorithm efficient with constant time complexity since the board is fixed.

## Algorithm (Rule-Based AI):

1. Initialize board with all blanks (2).
2. Define functions to check rows, columns, and diagonals using multiplicative encoding.
3. Implement Posswin() function:
    Returns the position where a player can win immediately.
4. Define AI strategy (playOdd()):
    First move → take corner.
    Second move → take center (if free).
    Third move → take opposite corner.
    After that:
        If player can win, take it.
        Else if opponent can win, block.
        Else pick best available move (corners, edges).
5. Print board after each move.
6. Continue until the board is full or a winner is found.

## Time Complexity Analysis:
Checking Rows/Columns/Diagonals: Each check is constant time (max 3 elements). → O(1)

Posswin() Function: Calls check functions → O(1)

playOdd() Execution: At most 9 moves, each making constant-time checks. → O(9) ≈ O(1)

Overall Time Complexity: O(1) (since the board size is fixed 3×3).
Space Complexity: O(1) (fixed board of 9 cells).

# Water Jug Problem using BFS

## Theory
The Water Jug Problem is a classical problem in Artificial Intelligence and Problem Solving. The task is to measure an exact quantity of water using two jugs of different capacities and a set of allowed operations. The allowed operations generally include:

1. Fill a jug completely.
2. Empty a jug completely.
3. Pour water from one jug into the other until either the first jug is empty or the second jug is full.

In this program, each state is represented as a pair (x, y), where x is the amount of water in Jug X and y is the amount of water in Jug Y. The initial state is (0, capacity_y) (first jug empty, second jug full in this case), and the goal is to reach any state where either x == target or y == target.

## Why BFS?

We use Breadth-First Search (BFS) to explore the state space because BFS guarantees finding the minimum number of steps to reach the solution. In BFS, nodes (states) are expanded level by level. A queue is used to keep track of unexplored nodes, and a set of visited states ensures we do not revisit previously explored configurations.

## State Generation

From any state (x, y), the possible next states (children) are generated by applying the allowed operations:
    Empty Jug X → (0, y)
    Empty Jug Y → (x, 0)
    Fill Jug X → (capacity_x, y)
    Fill Jug Y → (x, capacity_y)
    Pour X → Y until X is empty or Y is full.
    Pour Y → X until Y is empty or X is full.

This ensures all legal configurations are explored systematically.

## Time Complexity

The maximum number of unique states is capacity_x × capacity_y, since each jug can hold from 0 to its maximum capacity. Therefore, the time and space complexity of the BFS approach is:

    O(capacity-x ​× capacity-y​)

This is efficient for small jug capacities, which is usually the case in practical scenarios.

## Conclusion

The BFS approach provides a systematic and optimal solution to the Water Jug Problem. By modeling the problem as a graph of states and transitions, we can guarantee the shortest path to the solution whenever it exists.