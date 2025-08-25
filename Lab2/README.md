# Lab – 2  

**Aim:**  
To implement the following AI problems and algorithms:  
1. Solving the 8-Puzzle Problem using Best First Search.  
2. Implementing Tic-Tac-Toe using the prewritten algorithm given in Rich and Knight/Zak.  
3. Program to generate a Magic Square.  
4. Solving the Water Jug Problem.  

---

## Theory  

### 1. 8-Puzzle using Best First Search  
The 8-puzzle problem consists of a 3×3 grid with 8 numbered tiles and one blank space.  
The goal is to reach the target state from a given initial configuration.  

**Best First Search** is a heuristic-based search strategy that uses an evaluation function to decide which node to expand next.  
- Common heuristic functions:  
  - Number of misplaced tiles  
  - Manhattan distance  

---

### 2. Tic-Tac-Toe using Prewritten Algorithm  
Tic-Tac-Toe is a two-player game played on a 3×3 grid where players alternately place **X** and **O** symbols.  
The objective is to form a row, column, or diagonal with the same symbol.  

The algorithm provided in **Rich and Knight/Zak** uses either:  
- A simple **rule-based** approach  
- Or a **minimax decision-making process** to evaluate the best move for the computer while considering the opponent’s responses.  

---

### 3. Water Jug Problem  
The Water Jug Problem involves two jugs of different capacities and the task is to measure an exact quantity of water using them.  

It is solved using **state space search**, where:  
- Each state represents the amount of water in the two jugs.  
- Valid operations include:  
  - Filling a jug  
  - Emptying a jug  
  - Pouring water from one jug to another  

---

## Algorithm  

### Best First Search for 8-Puzzle  
- Create a priority queue (OPEN list), ordered by heuristic value (h).
- Insert the initial state into the queue.
- Create a set (CLOSED list) to store visited states.
- While the priority queue is not empty, repeat:
   Remove (pop) the state with the lowest heuristic value (best state)
    If this state is the goal state → return SUCCESS (solution found).
   Mark the current state as visited 
      - Add it to the CLOSED list.
   Expand the current state:
      - Generate all possible valid child states (next moves)
   For each child state:
      If the child is not in CLOSED (not already visited):
         - Calculate its heuristic value h(child).
         - Insert the child into the priority queue (OPEN list).
         - Optionally, keep track of parent pointers to reconstruct the path.
If the queue becomes empty and no goal was found:
   - Return FAILURE (no solution exists).
  

---

### Tic-Tac-Toe  
Turn 1:
- Play at corner (1).
Turn 2:
- If center (5) is empty → play at 5.
- Else → play at corner (1).
Turn 3:
- If corner (9) is empty → play at 9.
- Else → play at corner (3).
Turn 4:
- If X can win → play winning move.
- Else if O can win → block winning move.
- Else if corner (7) is empty → play at 7.
- Else → play at corner (3).
Turn 5:
- If X can win → play winning move.
- Else if O can win → block winning move.
- Else → play a strategic position (Make2).
Turn 6:
- If O can win → block winning move.
- Else if X can win → play winning move.
- Else → play a strategic position (Make2).
Turn 7:
- If X can win → play winning move.
- Else if O can win → block winning move.
- Else → play any empty spot.
Turn 8:
- If O can win → block winning move.
- Else if X can win → play winning move.
- Else → play any empty spot.
Turn 9:
- If X can win → play winning move.
- Else if O can win → block winning move.
- Else → play any empty spot.


---

### Water Jug Problem  
- Represent each state as (x, y):
     where x = current amount of water in Jug1
      y = current amount of water in Jug2.
- Start with the initial state (0, 0).
- Create a queue (for BFS) or stack (for DFS) to store states.
- Keep a set (Visited) to record states already explored.
- Store parent information to reconstruct the solution path.
- The target state is reached when either jug contains the required amount.

 From a state (x, y), possible next states are:
   a. Fill Jug1 → (jug1_capacity, y)
   b. Fill Jug2 → (x, jug2_capacity)
   c. Empty Jug1 → (0, y)
   d. Empty Jug2 → (x, 0)
   e. Pour Jug1 → Jug2:
        - Transfer min(x, jug2_capacity - y)
   f. Pour Jug2 → Jug1:
        - Transfer min(y, jug1_capacity - x)
Search Procedure (using BFS):
   a. Insert initial state (0, 0) into queue.
   b. While queue is not empty:
      i. Remove the front state (x, y).
      ii. If (x, y) is the goal → stop and reconstruct solution.
      iii. Otherwise, generate all valid successor states.
      iv. For each successor:
          - If not in Visited, mark as visited and insert into queue.

   - If goal found → return the sequence of operations (solution path).
   - If queue is empty → return failure (no solution exists).

---

## Time and Space Complexity  

### Best First Search for 8-Puzzle  
- **Time Complexity:** O(b^d), where b is branching factor and d is depth of solution.  
- **Space Complexity:** O(b^d).  

### Tic-Tac-Toe  
- **Time Complexity:** O(1) (Game finishes in 9 moves).  
- **Space Complexity:** O(1) (just stores the board).  

### Water Jug Problem  
- **Time Complexity:** O(|V| + |E|), where V = set of possible states, E = transitions.  
- **Space Complexity:** O(|V|).  

---

## Conclusion  
- **Best First Search** efficiently solves the 8-puzzle by using heuristics, but it does not guarantee the optimal solution unless an admissible heuristic is used.  
- **Tic-Tac-Toe** implementation demonstrates rule-based/minimax decision-making for game playing.  
- **Water Jug Problem** illustrates state space search and problem-solving strategies using simple operations, applicable to real-world resource measurement problems.  
