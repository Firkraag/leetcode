#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        d = dict()
        vertices = []
        n = len(prerequisites)
        edges = []
        for i, j in prerequisites:
            if i not in d:
                u = Vertex(i)
                vertices.append(u)
                d[i] = u
            else:
                u = d[i]
            
            if j not in d:
                v = Vertex(j)
                vertices.append(v)
                d[j] = v
            else:
                v = d[j]
            
            edges.append((u, v))
        
        graph = Graph(vertices, edges)
        return not graph.isCyclic()
        
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
    
       
    def isCyclic(self):
        global time
        for u in self.vertices:
            u.color = 0
            u.p = None
        time = 0
        for u in self.vertices:
            if u.color == 0:
                if self._dfs_visit(u):
                    return True
        return False
    def _dfs_visit(self, u):
        global time
        time = time + 1
        u.d = time
        u.color = 1
        for v in self.adj[u]:
            if v.color == 0:
                v.p = u
                if self._dfs_visit(v):
                    return True
            elif v.color == 1:
                return True
        u.color = 2
        time = time + 1
        u.f = time
        return False
