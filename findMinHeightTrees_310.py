class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 0:
            return []
        vertices = []
        edgeList = []
        for i in range(n):
            u = Vertex(i)
            vertices.append(u)

        for i, j in edges:
            edgeList.append((vertices[j], vertices[i]))
        
        graph = Graph(vertices, edgeList)
        return graph.mht()
      
class Vertex(object):
    def __init__(self, key):
        self.key = key

class Graph(object):
    def __init__(self, vertices = tuple(), edges = tuple()):
        self.vertices = set(vertices)
        self.adj = dict()
        for u in vertices:
            self.adj[u] = set()
        for u, v in edges:
            self._addEdge(u, v)
            
    def _addEdge(self, u, v):
        self.adj[u].add(v)
        self.adj[v].add(u)

    def bfs(self, s):
        from collections import deque
        
        for u in self.vertices:
            u.color = 0
            u.p = None
        s.color = 1
        s.p = None
        q = deque()
        q.append(s)
        while len(q) != 0:
            u = q.popleft()
            for v in self.adj[u]:
                if v.color == 0:
                    v.color = 1
                    v.p = u
                    q.append(v)
            u.color = 2

    def height(self, u):
        from collections import deque
        maximum = 0
        for v in self.adj[u]:
            if v.p == u:
                maximum = max(maximum, self.height(v) + 1)
        u.h = maximum
        return u.h
        
    def mht(self):
        s = next(iter(self.vertices))
        self.bfs(s)
        self.height(s)
        from collections import deque
        q = deque()
        s.pHeight = 0
        s.mh = s.h
        for u in self.adj[s]:
            q.append(u)
            if s.h == u.h + 1:
                s.vertex = u
        while len(q) != 0:
            u = q.popleft()
            v = u.p
            w = v.vertex
            if w != u:
                u.vertex = v
                u.mh = v.mh + 1
                u.pHeight = u.mh
            else:
                maximum = float("-Inf")
                for w in self.adj[v]:
                    if w != u and w.p == v:
                        if w.h + 2 > maximum:
                            maximum = w.h + 2
                u.pHeight = max(maximum, v.pHeight + 1)
                if u.pHeight >= v.mh - 1:
                    u.mh = u.pHeight
                    u.vertex = v
                else:
                    u.mh = v.mh - 1
                    for v in self.adj[u]:
                        if v.p == u and u.mh == v.h + 1:
                            u.vertex = v
            
            for v in self.adj[u]:
                if v.p == u:
                    q.append(v)
        minimum = min([u.mh for u in self.vertices])
        ret = []
        for u in self.vertices:
            if u.mh == minimum:
                ret.append(u.key)
        return ret
