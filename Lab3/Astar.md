## AIM
To implement the A* Search algorithm for pathfinding in a grid-based environment, demonstrating how heuristic and cost functions can be combined to find the optimal path efficiently.

## THEORY
A* Search is an informed search algorithm widely used in pathfinding and graph traversal problems. It is a best-first search algorithm that finds the least-cost path from a given start node to a goal node. The algorithm uses a heuristic function to estimate the cost from the current node to the goal. Each node maintains three cost values:
- g(n): The actual cost from the start node to the current node.
- h(n): The heuristic cost from the current node to the goal.
- f(n): The total estimated cost (f(n) = g(n) + h(n)).
The algorithm expands the node with the smallest f(n) value first, combining both cost-so-far and estimated cost-to-goal. This ensures optimality and completeness when the heuristic function is admissible (never overestimates the true cost).

## PROCEDURE
1. Initialize the grid map, defining blocked (obstacle) and free cells.
2. Define the start (source) and goal (destination) positions.
3. Create the initial node with g = 0, calculate h using the heuristic (Manhattan distance), and compute f = g + h.
4. Insert the start node into the open list (priority queue based on f value).
5. Repeat until the goal is found or the open list is empty:
   a. Select the node with the lowest f value (best candidate).
   b. Generate all valid neighboring nodes (up, down, left, right).
   c. Compute their g, h, and f values.
   d. If a neighbor is not visited, add it to the open list.
   e. Mark the current node as visited.
6. If the destination node is reached, reconstruct the path using parent pointers.
7. Display the explored nodes and the optimal path found.



## PSUDOCODE
function A_Star(start, goal):
    open_list = [start]
    closed_list = []
    g[start] = 0
    h[start] = heuristic(start, goal)
    f[start] = g[start] + h[start]

    while open_list is not empty:
        current = node with lowest f in open_list
        if current == goal:
            return reconstruct_path(current)
        
        open_list.remove(current)
        closed_list.append(current)

        for neighbor in neighbors(current):
            if neighbor in closed_list:
                continue

            tentative_g = g[current] + distance(current, neighbor)

            if neighbor not in open_list or tentative_g < g[neighbor]:
                parent[neighbor] = current
                g[neighbor] = tentative_g
                h[neighbor] = heuristic(neighbor, goal)
                f[neighbor] = g[neighbor] + h[neighbor]
                if neighbor not in open_list:
                    open_list.append(neighbor)
    return failure

## TIME COMPLEXITY
The time complexity of A* Search depends on the branching factor (b), the depth of the solution (d), and the quality of the heuristic function. In the worst case, it explores all nodes, resulting in O(b^d). However, with a good heuristic (like Manhattan distance), A* significantly reduces the search space and performs much faster in practice.

## SPACE COMPLEXITY
A* Search maintains both the open and closed lists during execution, which can contain most of the nodes in the search space. Thus, its space complexity is O(b^d), similar to its time complexity. This makes A* memory-intensive for large or dense maps.

## USE CASE
A* Search is widely used in fields requiring efficient pathfinding and navigation, such as:
- Robotics (autonomous robot navigation)
- Game Development (NPC movement, AI pathfinding)
- Geographic Information Systems (shortest route computation)
- Network routing and optimization
- Puzzle solving (e.g., 8-puzzle, 15-puzzle problems)

## CONCLUSION
The A* Search algorithm efficiently finds the optimal path between two points using both actual and estimated costs. Its use of heuristics makes it faster than uninformed algorithms like Dijkstra’s or BFS, while still guaranteeing the shortest path when the heuristic is admissible. Though memory-intensive, A* remains one of the most effective and widely used algorithms for optimal pathfinding.

