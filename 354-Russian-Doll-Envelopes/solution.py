class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        vertices = [None] * n
        for i in range(n):
            vertices[i] = Vertex(i)
        edges = []
        for i in range(n):
            width1, height1 = envelopes[i]
            for j in range(i + 1, n):
                width2, height2 = envelopes[j]
                if width1 <width2 and height1 < height2:
                    edges.append((vertices[i], vertices[j]))
                elif width2 < width1 and height2 < height1:
                    edges.append((vertices[j], vertices[i]))
        # It is a directed acylic graph
        graph = Graph(vertices, edges)
        return graph.longestSimplePathLength()

class Vertex(object):
    def __init__(self, key):
        self.key = key

class Graph(object):
    def __init__(self, vertices = tuple(), edges = tuple(), directed = True):
        self.directed = directed
        self.vertices = set(vertices)
        self.edges = set()
        self.adj = dict()
        for u in vertices:
            self.adj[u] = set()
        for u, v in edges:
            self._addEdge(u, v)

    def _addEdge(self, u, v):
        if self.directed:
            self.adj[u].add(v)
            self.edges.add((u, v))
        elif u != v: # undirected graph does not allow self loop
            self.adj[u].add(v)
            self.edges.add((u, v))
            self.adj[v].add(u)
            self.edges.add((v, u))

    def longestSimplePathLength(self):
        global maxLength
        for u in self.vertices:
            u.color = 0
        maxLength = 1
        for u in self.vertices:
            if u.color == 0:
                self._dfs_visit(u)
        return maxLength
    
    def _dfs_visit(self, u):
        global maxLength
        u.color = 1
        maximum = 1
        for v in self.adj[u]:
            if v.color == 0:
                maximum = max(maximum, 1 + self._dfs_visit(v))
            elif v.color == 2:
                maximum = max(maximum, 1 + v.length)
        u.color = 2
        u.length = maximum
        maxLength = max(u.length, maxLength)
        return maximum
