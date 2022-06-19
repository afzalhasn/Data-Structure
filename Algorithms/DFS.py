
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def BFS(self,s):
        queue = deque()
        visited = [False]*(max(self.graph)+1)
        visited[s] = True
        queue.append(s)
        while queue:
            v = queue.popleft()
            print(v,end=' ')
            for i in self.graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
    def DFS(self,s,visited):
        visited.add(s)
        print(s,end=" ")
        for a in self.graph[s]:
            if a not in visited:
                self.DFS(a,visited)

    def DFSUtil(self,s):
        visited = set()
        self.DFS(s,visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print("Following is BFs/DFS from (starting from vertex 2)")
print(g.graph)
g.DFSUtil(2)
print()
# g.BFS(2)
