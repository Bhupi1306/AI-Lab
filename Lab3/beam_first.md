
## AIM:
To implement and understand the working of the Beam Search algorithm for efficient pathfinding in a grid-based map.

## THEORY:
Beam Search is a heuristic-based search algorithm derived from the Best-First Search strategy. Unlike A* or BFS which explore all nodes, Beam Search restricts the number of nodes considered at each level by using a parameter called 'beam width'. At every step, only a fixed number of best nodes (based on heuristic value) are expanded, which reduces memory consumption and speeds up execution. 
However, this trade-off can lead to suboptimal paths if the best path is pruned early. Beam Search is widely used in fields like Natural Language Processing, speech recognition, and robotics for large state-space problems.

## PROCEDURE:
1. Initialize a grid representing the environment with obstacles and free cells.
2. Define the source (start) and destination (goal) positions.
3. Compute the heuristic value for the source node (e.g., Manhattan distance to goal).
4. Insert the source node into the open list (priority queue).
5. While the open list is not empty:
   - Remove the node with the lowest f = g + h value.
   - Generate all valid neighboring nodes (up, down, left, right).
   - Compute their heuristic and cost values.
   - Select only the top 'k' nodes (based on beam width) and add them to the open list.
6. Repeat until the goal is found or the open list becomes empty.
7. If the goal is reached, output the path; otherwise, report that no path exists.

## ALGORITHM USED:
1. Start with the initial node (source position) and calculate its heuristic value.
2. Initialize the open list (priority queue) with the starting node.
3. Repeat until the goal is found or the open list becomes empty:
   - Select the best node (lowest f = g + h value) from the open list.
   - Generate all possible child nodes from the current node.
   - Sort these child nodes by their heuristic value.
   - Keep only the top k nodes (where k = beam width) to limit the search space.
   - Add these k nodes to the open list if they have not been visited.
4. If the goal node is reached, trace back the path from goal to start.
5. Else, if the open list becomes empty, terminate — no solution exists.
Time and Space Complexity:
Let 'b' be the branching factor, 'd' be the depth of the goal node, and 'k' be the beam width.
• Time Complexity: O(k × d)
• Space Complexity: O(k × d)
Since only 'k' nodes are maintained at each level, Beam Search is more memory-efficient than A*, but may miss the optimal solution due to pruning.

## USE CASE:
Beam Search is often applied in Natural Language Processing tasks such as text generation, machine translation, and speech recognition where exploring all possible sequences is computationally infeasible. It is also used in pathfinding problems for robotics and AI-based navigation systems.

## CONCLUSION:
Beam Search offers a trade-off between efficiency and accuracy. By limiting the number of nodes explored at each step, it significantly reduces computation time and memory usage, making it suitable for large and complex search spaces. However, due to its pruning mechanism, it may fail to find the optimal solution if the correct path is discarded early.


 
