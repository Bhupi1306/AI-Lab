## AIM
To implement the Blocks World problem using State Space Search in Prolog to generate a valid sequence of actions that transforms the initial state into the goal state.

## THEORY
The Blocks World problem is a classic example in Artificial Intelligence used to demonstrate state-space search and planning. It consists of a set of blocks placed on a table, and the goal is to achieve a specific configuration by moving blocks according to defined rules. A state represents the current arrangement of blocks, and an action transforms one state into another. 

In this program, Prolog is used to represent states, actions, and goals declaratively. The search algorithm recursively explores possible states by applying valid actions until the goal state is satisfied. This approach demonstrates how logical reasoning and backtracking can be used for automated planning.

## ALGORITHM
1. Define all possible blocks and actions (pickup, putdown, stack, unstack).
2. Represent each state as a list of facts describing the positions and conditions of blocks.
3. Define preconditions and effects for each action.
4. Implement predicates to check whether an action is applicable in the current state.
5. Apply the action to generate a new state by adding and deleting facts.
6. Avoid redundant or cyclic moves using visited state checks.
7. Recursively search through the state space until the goal conditions are satisfied.
8. Output the sequence of actions (plan) leading from the initial state to the goal state.

## PROCEDURE
1. Define all blocks and possible actions in Prolog.
2. Specify the initial and goal states.
3. Define the 'applicable' predicate to check action feasibility.
4. Define the 'apply' predicate to transition from one state to another.
5. Implement 'plan_search' to recursively explore states until the goal is achieved.
6. Test the program using predefined test cases (simple, tower, and complex goals).
7. Observe the generated sequence of actions that achieves the goal configuration.


## TIME AND SPACE COMPLEXITY
Let b be the branching factor (number of applicable actions per state) and d be the depth of the goal state.
• Time Complexity: O(b^d), as each possible action leads to a new branch in the search tree.
• Space Complexity: O(b^d), since all generated states and paths must be stored during search.
These complexities can be reduced with pruning or heuristic techniques such as A* search.

## USE CASE
The Blocks World problem models real-world AI planning systems such as robot manipulation, task sequencing, and automated assembly. It demonstrates how declarative logic and search can be used to plan multi-step actions efficiently.

## CONCLUSION
The Blocks World problem was successfully implemented in Prolog using state-space search. The program generates an optimal sequence of actions that transforms the initial configuration into the desired goal. This experiment illustrates how Prolog’s logical reasoning and recursive search capabilities can be used for AI planning problems.
