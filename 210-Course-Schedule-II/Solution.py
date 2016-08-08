class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        d = dict()     
        vertices = []
        n = len(prerequisites)
        edges = []
        for i in range(numCourses):
            u = Vertex(i)
            vertices.append(u)
            d[i] = u
            
        for i, j in prerequisites:
            edges.append((d[j], d[i]))
        
        graph = Graph(vertices, edges)
        orders = graph.topologicalSort()
        if len(orders) == 0:
            return []
        else:
            return orders
         
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
    
       
    def topologicalSort(self):
        n = len(self.vertices)
        orders = [None] * n
        # The graph is cyclic
        if self.dfs(orders):
            return []
        else:
            return orders
    
    def dfs(self, orders):
        global time
        global index
        
        n = len(orders)
        for u in self.vertices:
            u.color = 0
            u.p = None
        time = 0
        index = n - 1
        for u in self.vertices:
            if u.color == 0:
                if self._dfs_visit(u, orders):
                    return True
        return False
    def _dfs_visit(self, u, orders):
        global time
        global index
        time = time + 1
        u.d = time
        u.color = 1
        for v in self.adj[u]:
            if v.color == 0:
                v.p = u
                if self._dfs_visit(v, orders):
                    return True
            elif v.color == 1:
                return True
        u.color = 2
        time = time + 1
        u.f = time
        orders[index] = u.key
        index -= 1
        return False
        
