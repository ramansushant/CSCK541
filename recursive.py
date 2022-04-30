def recursive_floyd_warshall(dist):
	v = len(graph)
	indices = range(v)

	for i in indices:
		for j in indices:
			if i == j:
				dist[i][j] = 0
			else:
				dist[i][j] = shortestpath(i, j, v - 1, dist)
	return dist


# Function to calculate the shortest path between
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
