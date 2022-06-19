from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.minCost = {}
        self.path = {}
        self.visited = set()
    def addEdge(self,src,dst,cost):
        self.graph[src].append((dst,cost))
        self.graph[dst].append((src,cost))
        self.minCost[src] = float('inf')
        self.minCost[dst] = float('inf')
        self.path[src] = []
        self.path[dst] = []
    def shortDistance(self,src,dst):
        self.path[src]  = src
        queue = [(src,0)]
        visited.add(src)
        while queue:
            s,c = queue.pop()
            for a in self.graph[s]:
                if a[0] not in visited:
                    queue.append(a)
                    visited.add(a[0])
                


g = Graph()
g.addEdge('A','B',2)
g.addEdge('A','C',4)
g.addEdge('B','C',3)
g.addEdge('B','D',8)
g.addEdge('D','E',11)
g.addEdge('D','F',22)
g.addEdge('C','D',2)
g.addEdge('C','E',5)
g.addEdge('E','F',1)
print(g.graph)
