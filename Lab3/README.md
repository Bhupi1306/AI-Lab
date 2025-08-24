
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
1. Insert start node into an open priority queue ordered by `f = g + h`.  
2. Repeat until the queue is empty:  
   - Remove node with lowest `f(n)`.  
   - If it is the goal → success.  
   - Else, generate successors.  
   - Compute `g, h, f` for successors.  
   - Insert if not visited.  
3. If queue is empty → failure.  

---

### Beam Search Algorithm
1. Start with the initial node in the open list.  
2. While open list is not empty:  
   - Expand best node.  
   - Generate successors.  
   - Keep only best `k` nodes (beam width).  
   - If goal found → success.  
3. If list empty → failure.  

---

### Hill Climbing Algorithm
1. Start with an initial state.  
2. Repeat until goal or no better state:  
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
