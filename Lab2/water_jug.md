##AIM
To implement and simulate the Water Jug Problem using the Breadth-First Search (BFS) algorithm to determine the sequence of states that leads to a desired quantity of water in one of the jugs.
##THEORY
The Water Jug Problem is a classic example of a state-space search problem in Artificial Intelligence. 
It involves two jugs with different capacities, and the goal is to obtain a target amount of water using a series of allowed operations. 
Each unique combination of water levels in the two jugs represents a state.

In this problem, we are given two jugs: Jug X (capacity = 3 liters) and Jug Y (capacity = 4 liters). 
The objective is to measure exactly 2 liters of water using the two jugs. The allowed operations are:
    • Fill a jug completely.
    • Empty a jug completely.
    • Pour water from one jug into the other until one becomes full or the other becomes empty.

The algorithm represents each state as an ordered pair (x, y), where x is the amount of water in Jug X and y is the amount in Jug Y.

To solve this, we use the Breadth-First Search (BFS) algorithm:
    1. Start from the initial state (0, 4).
    2. Generate all possible successor states using the allowed operations.
    3. Push each new, unvisited state into a queue for exploration.
    4. If a state satisfies the goal condition (x == target or y == target), the solution is found.
    5. Continue exploring until all possible states are visited or the goal is achieved.

BFS is particularly suited for this problem because it explores states level by level, ensuring the shortest sequence of actions is found.



##PROCEDURE
1. Initialize both jugs with zero or specified starting water levels.
2. Define the goal quantity to be measured (e.g., 2 liters).
3. Represent each state as a pair (x, y), where x and y are the water amounts in Jug X and Jug Y respectively.
4. Use a queue to perform Breadth-First Search:
   a. Dequeue a state and check if it satisfies the goal.
   b. Generate all possible next states by applying the operations:
      • Fill a jug.
      • Empty a jug.
      • Pour water from one jug to another.
   c. For each new state not visited earlier, enqueue it.
5. Repeat until the goal state is reached or all possibilities are explored.
6. Display the state transitions and the final result.

##TIME COMPLEXITY
Let Cx and Cy be the capacities of the two jugs.
In the worst case, each unique combination of (x, y) is explored once.
Therefore, the total number of states = (Cx + 1) × (Cy + 1).
Hence, the time complexity of BFS is O(Cx × Cy).

##SPACE COMPLEXITY
Since BFS stores all generated states in a queue and a visited set, the space complexity is also proportional to the total number of states.
Space Complexity: O(Cx × Cy).

##USE CASE
The Water Jug Problem illustrates fundamental search strategies in Artificial Intelligence and Problem Solving. It is used in AI education to demonstrate state-space representation, graph traversal, and uninformed search techniques. It also serves as a foundation for real-world applications such as resource distribution, scheduling, and optimization problems.

##CONCLUSION
The Water Jug Problem was successfully implemented using the Breadth-First Search algorithm. The program systematically explores all possible states of the two jugs and identifies the shortest sequence of operations to measure the target quantity of water. This experiment demonstrates the practical application of BFS in solving state-space search problems efficiently.
