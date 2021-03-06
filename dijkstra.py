import math
import numpy as np
import pandas as pd
from collections import deque
import sys
import time


def load_graph(graph_file):
	"""
	The graph is stored in a .csv file in the form of an adjacency matrix.
	:param graph_file: the name of the graph .csv file
	:type graph_file: String
	:return: the graph as adjacency matrix
	:rtype: numpy.ndarray
	"""

	graph = pd.read_csv(graph_file, header=None)
	graph = graph.values
	return graph


def dijkstra(graph, s, t):
	"""
	This function implements the main Dijkstra algorithm routine.
	:param graph: the graph in the form of adjacency matrix
	:type graph: numpy.ndarray
	:param s: the source node
	:type s: int
	:param t: the target node
	:type t: int
	:return: the shortest sequence of nodes (path) to reach target from source
	:rtype: collections.deque
	"""

	N = graph.shape[0]
	dist = {k:math.inf for k in range(N)}
	prev = np.array(N * [None])
	q = set(list(range(N)))
	dist[s] = 0

	while q:
		temp_dist = {k:dist[k] for k in q}
		u = min(temp_dist, key = temp_dist.get)
		q.remove(u)
		if u == t:
			break

		# neighbors of u
		neighbors = graph[u, :].nonzero()[0]
		for v in neighbors:
			alt = dist[u] + graph[u, v]
			if alt < dist[v]:
				dist[v] = alt
				prev[v] = u

	S = deque()
	u = t
	if (prev[u] is not None) or (u == s):
		while (u is not None):
			S.append(u)
			u = prev[u]

	return S


def main():
	"""
	The main function of the script.
	"""

	# Read input
	mode = int(sys.argv[1])
	if mode == 0:
		graph_file = 'graph.csv'
		graph = load_graph(graph_file)
	elif mode == 1:
		N = 10000
		graph = np.random.randint(1, 10, size = (N, N))
		graph = (graph + graph.T) / 2
	else:
		print('First argument should be either 0 (read graph from file) or 1 (generate random graph).')
		return

	s = int(sys.argv[2])

	t = int(sys.argv[3])

	# Run algorithm
	start_time = time.time()
	S = dijkstra(graph, s, t)
	end_time = time.time()

	# Print results
	print('Elapsed time (sec.): ', end_time - start_time)
	shortest_path_length = 0
	for i in range(len(S) - 1):
		shortest_path_length += graph[S[i], S[i+1]]
	print('Shortest path length: ', shortest_path_length)
	print('Shortest path: ', end = ' ')
	while len(S) != 0:
		print(S.pop(), end = ' ')
		if len(S) != 0:
			print('=>', end = ' ')


if __name__ == '__main__':
	main()