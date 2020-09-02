Native Python implementation of Dijkstra's algorithm.

https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

This implementation (at its current phase) does not include a priority queue.

Usage:

1. Directly from terminal:
python dijkstra.py A B C

2. From ipython:
%run dijkstra.py A B C

Arguments:

1. A: This is the execution mode. It can take 2 values, namely 0 which means that the script should use as graph the one stored in graph.csv file, and 1 which means that a random graph (in the form of a random symmetric numpy array of integers) will be used.

2. B: the source node (as integer)

3. C: the target node (as integer)

Example: for a graph with N = 10 nodes stored in graph.csv file, source = 0 and target = 5 the execution command will be (from within ipython):

%run dijkstra.py 0 0 5