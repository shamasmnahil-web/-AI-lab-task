"""
# A* Search and Uniform Cost Search (UCS)

A small Python example comparing A* Search and Uniform Cost Search on a weighted graph. It also shows how an overestimated heuristic can affect A*.

## Overview

The program searches for the lowest-cost path from start node S to goal node G.

- A* Search ranks paths using f(n) = g(n) + h(n).
- Uniform Cost Search (UCS) ranks paths by the accumulated cost g(n).

Here, g(n) is the cost so far and h(n) estimates the remaining cost to the goal.

## Graph

| Edge | Cost |
| --- | ---: |
| S -> A | 1 |
| S -> B | 4 |
| A -> C | 2 |
| B -> G | 5 |
| C -> G | 3 |

The lowest-cost route with the original heuristic is S -> A -> C -> G, with total cost 6. The alternative route S -> B -> G costs 9.

## Requirements

- Python 3
- No external packages; the program uses Python's built-in heapq module.

## How to Run

Save the provided program as main.py, then run it from a terminal:

    python3 main.py

On some Windows systems, use:

    python main.py

## Expected Output

    A*: (['S', 'A', 'C', 'G'], 6)
    UCS: ('S->A->C->G', 6)
    Overestimated: (['S', 'B', 'G'], 9)

A* returns its path as a list, while UCS returns its path as a string.

## Heuristic Demonstration

The original heuristic values are:

| Node | h(n) |
| --- | ---: |
| S | 5 |
| A | 4 |
| B | 4 |
| C | 2 |
| G | 0 |

The final test changes h(C) to 10. This overestimates the remaining cost from C to G, so A* chooses S -> B -> G with cost 9 instead of the optimal cost 6. This demonstrates why heuristic quality matters. An admissible heuristic never overestimates the actual remaining cost.

## Algorithms

A* uses a priority queue and expands the path with the smallest estimated total cost, g(n) + h(n). UCS uses a priority queue ordered by the cost accumulated so far. With non-negative edge costs, UCS finds a lowest-cost path.

## Repository Files

- README.py - this project description
- main.py - save the provided A* and UCS program here
"""
