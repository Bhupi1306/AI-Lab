## AIM
To implement the Hill Climbing Search algorithm for solving the 8-puzzle problem, demonstrating how heuristic-based local search can be used to reach an optimal or near-optimal solution.

## THEORY
Hill Climbing is a heuristic search algorithm used for mathematical optimization problems. It starts with an arbitrary solution and iteratively makes incremental changes to the solution, selecting the neighbor with the lowest heuristic (or cost) value. The process continues until no better neighbors exist, indicating a local optimum. However, the algorithm can get stuck in local maxima, plateaus, or ridges, which makes it less reliable for problems with complex search spaces.
In this experiment, the algorithm is applied to the 8-puzzle problem, where the objective is to arrange tiles in order so that they match a predefined goal configuration. The heuristic function (h-value) is based on the Manhattan distance, which measures how far each tile is from its correct position.

## PROCEDURE
1. Initialize the 8-puzzle problem with a start state.
2. Define the goal state (solution matrix).
3. Compute the heuristic (h-value) using Manhattan distance for each tile.
4. Generate all possible children (neighbor states) by moving the blank tile (0) up, down, left, or right.
5. Select the child with the lowest heuristic value as the next current state.
6. Repeat the process until:
   - The goal state is reached, or
   - No child has a lower heuristic value (local maxima reached).
7. Display the final configuration and terminate.

## ALGORITHM

function hill_climbing(initial_state):
    current = initial_state
    while True:
        neighbors = generate_successors(current)
        if neighbors is empty:
            return current
        next_state = neighbor with lowest heuristic
        if heuristic(next_state) >= heuristic(current):
            return current
        current = next_state

## TIME COMPLEXITY
The time complexity of Hill Climbing depends on the number of possible states and neighbors generated. For the 8-puzzle problem, each state can generate up to 4 neighbors. In the worst case, the algorithm explores all states until reaching a plateau or the goal. Thus, the time complexity is approximately O(b^d), where b is the branching factor (≈4) and d is the depth of the search.

## SPACE COMPLEXITY
Since Hill Climbing keeps track of only the current state and its immediate neighbors, its space complexity is O(b), where b is the number of neighbors (≈4 for the 8-puzzle problem). This makes it more memory-efficient compared to algorithms like A* or BFS.

## USE CASE
Hill Climbing is widely used in optimization and search problems such as:
- Solving puzzles (e.g., 8-puzzle, N-Queens problem)
- Pathfinding and navigation
- Scheduling and resource allocation
- Feature selection in Machine Learning
- Game AI decision-making systems

## CONCLUSION
The Hill Climbing Search algorithm provides a simple yet effective method for heuristic search in optimization problems. It efficiently finds solutions in small or smooth search spaces but can get trapped in local maxima or plateaus. Despite its limitations, it is a foundational concept for more advanced algorithms like Simulated Annealing and Genetic Algorithms.
