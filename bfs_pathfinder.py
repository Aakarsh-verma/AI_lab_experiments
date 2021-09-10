from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def BFS(self, s):
		visited = [False] * (max(self.graph) + 1)

		queue = [s]
		visited[s] = True

		while queue:

			s = queue.pop(0)
			print (s, end = " ")

			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

def main():
	# Create a Graph
	g = Graph()
	n = int(input("Enter no. of edges: "))
	for _ in range(n):
		edges = list(map(int, input("Enter edge (x, y): ").rstrip().split(',')))
		g.addEdge(edges[0], edges[1])

	# Call BFS
	v = int(input("Following is Breadth First Traversal (Enter Strating vertex) : "))
	g.BFS(v)

if __name__ == "__main__":
	main()