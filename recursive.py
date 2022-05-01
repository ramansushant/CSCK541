def recursive_floyd_warshall(dist):
	v = len(graph)
	indices = range(v)

# compute all-pairs shortest paths
	for i in indices:
		for j in indices:
			if i == j:
				dist[i][j] = 0
			else:
				dist[i][j] = shortestpath(i, j, v - 1, dist)
	return dist


# Finds the shortest path from i to j using only vertices 0 through k as intermediaries
def shortestpath(i, j, k, dist):
	if k < 0:
		return (dist[i][j])
	else:
		return min(shortestpath(i, j, k - 1, dist), shortestpath(i, k, k - 1, dist) + shortestpath(k, j, k - 1, dist))


# Input Sample Data
# INF is used for the vertices not connected directly. A large value is assigned to this variable
INF = 9999
graph = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]

# Print Output
print(recursive_floyd_warshall(graph))
