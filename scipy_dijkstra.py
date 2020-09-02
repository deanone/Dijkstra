import sys
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
import time


def main():
	N = 10000
	s = int(sys.argv[1])
	t = int(sys.argv[2])
	graph = np.random.randint(1, 10, size = (N, N))
	graph = (graph + graph.T) / 2
	graph = graph.astype('int')
	graph = csr_matrix(graph)

	start_time = time.time()
	dijkstra(csgraph=graph, directed=False, indices=s, return_predecessors=True)[0][t]
	end_time = time.time()
	print('Elasped time (sec.): ', end_time - start_time)

if __name__ == '__main__':
	main()