Problem Statement:
We have been given a 5x5 grid consisting of numbers 1-25 that are not in the right order. 
Our solution should aim at restoring the normal configuration of the board by performing a set legal moves which are Inner ring counter clock movement, Inner ring counter clock wise movement, Outer ring counter clock movement, Outer ring clock wise movement.
The solution should be reached in minimum number of moves.


Approach:
We employ A* search to implement a solution for this problem.

The state space for this problem is : 25
Heuristic function h(s) = Sum of Manhattan distance between current position and goal position for all numbers in the grid
Cost incurred to move to next state g(s) = Number of rotations or wraps done so far.
Cost = Sum of h(s) and g(s)


We start with an initial state and do a set of operations mentioned below:
1. Right wrap (on all five rows)
2. Left wrap (on all five rows)
3. Up shift wrap (on all five colomns)
4. Down shift wrap (on all five colomns)
5. Inner ring clockwise rotation
6. Outer ring clockwise rotation
7. Inner ring counter cloclwise rotation
8. Outer ring counter clockwise rotation

We calculate the cost incurred by executing each of the above moves mentioned and append them to a list of successors. These successors are appended to a fringe. On popping from the fring the successor with the least cost incurred is obtained and we check whether this is a goal state. If this is not a goal state we proceed to explore successors of this current successor. Cost is calculated for each state and appended to the fringe and each time a successor with the least cost is explored. We continue this process until we reach the goal state.
