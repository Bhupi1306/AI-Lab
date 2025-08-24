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
1. Start with the initial state and insert it into a priority queue ordered by heuristic value.  
2. Repeat until the queue is empty:  
   i. Remove the node with the lowest heuristic value.  
   ii. If it is the goal state, return success.  
   iii. Otherwise, generate all valid child states.  
   iv. Insert the child states into the priority queue if not already visited.  

---

### Tic-Tac-Toe  
1. Initialize an empty 3×3 board.  
2. While the game is not over:  
   i. If it is the computer’s turn, use the algorithm (rule-based/minimax) to choose the optimal move.  
   ii. If it is the player’s turn, accept input and update the board.  
   iii. Check if either player has won or if the board is full.  
3. Declare the result as win, lose, or draw.  

---

### Water Jug Problem  
1. Represent the state as **(x, y)** where:  
   - x = amount in jug1  
   - y = amount in jug2  
2. Start from the initial state (0,0).  
3. Generate successor states using valid operations: fill, empty, or pour.  
4. Use BFS or DFS to explore states until the target state is found.  
5. Return the sequence of operations leading to the solution.  

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
