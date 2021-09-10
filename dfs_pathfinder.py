from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)


	def addEdge(self, u, v):
		self.graph[u].append(v)

	def DFSUtil(self, v, visited):
		visited.add(v)
		print(v, end=' ')

		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)

	def DFS(self, v):

		visited = set()

		self.DFSUtil(v, visited)

def main():
	g = Graph()
	n = int(input("Enter no. of edges: "))
	for _ in range(n):
		edges = list(map(int, input("Enter edge (x, y): ").rstrip().split(',')))
		g.addEdge(edges[0], edges[1])

	v = int(input("Following is Depth First Traversal (Enter Strating vertex) : "))
	g.DFS(v)

if __name__ == "__main__":
	main()