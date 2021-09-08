from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def BFS(self, s):
		# Mark all the vertices as not visited
		visited = [False] * (max(self.graph) + 1)
		# Create a queue for BFS
		queue = [s]
		visited[s] = True

		while queue:
			# Dequeue a vertex from queue and print
			s = queue.pop(0)
			print (s, end = " ")

			# Get all adjacent vertices s. If a adjacent has not been visited, 
            # then mark it visited and enqueue
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

# Create a Graph
g = Graph()
n = int(input("Enter no. of edges: "))
for _ in range(n):
    edges = list(map(int, input("Enter edge (x, y): ").rstrip().split(',')))
    g.addEdge(edges[0], edges[1])
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)

# Call BFS
v = int(input("Following is Breadth First Traversal (Enter Strating vertex) : "))
g.BFS(v)