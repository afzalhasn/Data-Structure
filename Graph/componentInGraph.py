from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

def componentsInGraph(gb):
    # Write your code here
    g = Graph()
    visited_set = set()
    for a,b in gb:
        g.addEdge(a,b)
    result = set()
    for a in g.graph:
        queue = []
        queue.append(a)
        if a in visited_set:
            continue
        myset = set()
        while queue:
            val = queue.pop()
            myset.add(val)
            visited_set.add(val)
            for v in g.graph[val]:
                if v not in visited_set:
                    queue.append(v)
                myset.add(v)
                visited_set.add(v)
        result.add(len(myset))

if __name__ == '__main__':
    # n = int(input().strip())

    # gb = []

    # for _ in range(n):
    #     gb.append(list(map(int, input().rstrip().split())))
    n = 5
    gb = [[1, 6],[2, 7], [3, 8], [4,9], [2, 6]]
    result = componentsInGraph(gb)
    # print(result)