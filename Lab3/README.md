
Where:  
- `g(n)` = actual cost from the start node to `n`  
- `h(n)` = heuristic estimate from `n` to the goal  
- `f(n)` = total estimated cost of the cheapest solution through `n`  

If the heuristic `h(n)` is **admissible** (never overestimates), A* guarantees the **optimal solution**.  

---

### Beam Search
Beam Search is a heuristic search algorithm that explores only a limited set of best nodes at each level, defined by a **beam width (k)**.  

- At each level:  
  - Generate all children of current nodes.  
  - Select only the **best k nodes**.  
- Continue until the goal is found or no nodes remain.  

**Pros:** Memory-efficient compared to A*.  
**Cons:** May discard optimal paths → not guaranteed optimal.  

---

### Hill Climbing
Hill Climbing is a local search algorithm inspired by the process of climbing a hill by always moving upwards (towards better heuristic values).  

- Start with an initial solution.  
- Generate neighbors and move to the best neighbor.  
- Repeat until no improvement is possible.  

**Limitations:** Can get stuck in  
- Local maxima  
- Plateaus  
- Ridges  

Variants like **Random Restart Hill Climbing** or **Simulated Annealing** can overcome these issues.  

---

## Algorithms

### A* Search Algorithm
- Place the initial state into a priority queue (OPEN list), ordered by f(n) = g(n) + h(n).
- Set g(start) = 0 and compute h(start), then f(start) = g(start) + h(start).
- Create a CLOSED set to store expanded (visited) states.
- Store parent pointers to reconstruct the path later.

- While OPEN is not empty:
  - Remove the state with the lowest f(n) value from OPEN (best candidate).
  - If this state is the goal:
    - Return success and reconstruct the solution path by following parent links.
  - Otherwise, expand the current state by generating all valid successors 
    (e.g., possible moves of the blank in case of the 8-puzzle).
  - For each successor:
    - Compute g(successor) = g(current) + step_cost(current, successor).
    - Compute h(successor) using the heuristic function.
    - Compute f(successor) = g(successor) + h(successor).
    - If the successor is not in CLOSED or OPEN:
      - Insert it into OPEN with its f, g, h values and record its parent.
    - Else if the successor is already in OPEN but this new path has a lower g value:
      - Update its g, f values and reset its parent to the current state.
  - Add the current state to CLOSED (mark as expanded).

- If OPEN becomes empty and the goal is not found:
  - Return failure (no solution exists)
 

---

### Beam Search Algorithm
- Place the start node in the OPEN list.
- Define the beam width k (maximum number of nodes to keep at each level).

- While the OPEN list is not empty:
  - Select and expand the best node(s) from the OPEN list.
  - Generate all possible successors of the expanded nodes.
  - Evaluate each successor using the heuristic function.
  - Sort the successors according to their heuristic values.
  - Keep only the best k successors (beam width restriction) and discard the rest.
  - Replace the OPEN list with these k nodes.

- If the goal state is present in the OPEN list:
  - Return success and reconstruct the path to the goal.

- If the OPEN list becomes empty and the goal is not found:
  - Return failure (no solution).

---

### Hill Climbing Algorithm
- Start with an initial state.  
- Repeat until goal or no better state:  
   - Generate neighbors.  
   - Choose neighbor with best heuristic.  
   - If better → move. Else stop.  

---

## Time and Space Complexity

- **A\***  
  - Time: `O(b^d)` (depends on heuristic)  
  - Space: `O(b^d)`  
  - **Optimal** with admissible heuristic  

- **Beam Search**  
  - Time: `O(b × k × d)`  
  - Space: `O(k × d)`  
  - **Not guaranteed optimal**  

- **Hill Climbing**  
  - Time: `O(b × d)`  
  - Space: `O(1)`  
  - May get stuck in local maxima  

---

## Conclusion
- **A\*** → Optimal and efficient with admissible heuristics.  
- **Beam Search** → Faster, memory-efficient, but sacrifices optimality.  
- **Hill Climbing** → Simple and efficient, but prone to local maxima and plateaus.  
