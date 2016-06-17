#!/usr/bin/env python
# coding=utf-8
class Vertex(object):
    def __init__(self, key):
        self.key = key

class Graph(object):
    def __init__(self, vertices = tuple(), edges = tuple(), directed = True):
        self.directed = directed
        self.adj = dict()
        for u in vertices:
            self.adj[u] = set()
        for u, v in edges:
            self._addEdge(u, v)

    def _addEdge(self, u, v):
        if self.directed:
            self.adj[u].add(v)
            
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        print m, n
        vertices = [[None] * n for i in range(m)]
        self.vertices = vertices
        for i in range(m):
            for j in range(n):
                vertices[i][j] = Vertex(matrix[i][j])
        edges = self.generateEdges(matrix, vertices)
        g = Graph([v for u in vertices for v in u], edges)
        return self.topologicalSort(g)
    
    def topologicalSort(self, graph):
        global maxLength
        for l in self.vertices:
            for u in l:
                u.color = 0
        maxLength = 1
        for l in self.vertices:
            for u in l:
                if u.color == 0:
                    self._dfs_visit(graph, u)
        return maxLength
        
    def _dfs_visit(self, graph, u):
        global maxLength
        u.color = 1
        maximum = 1
        for v in graph.adj[u]:
            if v.color == 0:
                maximum = max(maximum, 1 + self._dfs_visit(graph, v))
            elif v.color == 2:
                maximum = max(maximum, 1 + v.length)
        u.color = 2
        u.length = maximum
        maxLength = max(u.length, maxLength)
        return maximum

    def generateEdges(self, matrix, vertices):
        m = len(matrix)
        n = len(matrix[0])
        edges = []
        for i in range(m):
            for j in range(n):
                value = matrix[i][j]
                vertex = vertices[i][j]
                if i > 0 and value < matrix[i - 1][j]:
                    edges.append((vertex, vertices[i - 1][j]))
                if i < m - 1 and value < matrix[i + 1][j]:
                    edges.append((vertex, vertices[i + 1][j]))
                if j > 0 and value < matrix[i][j - 1]:
                    edges.append((vertex, vertices[i][j - 1]))
                if j < n - 1 and value < matrix[i][j + 1]:
                    edges.append((vertex, vertices[i][j + 1]))
        return edges
                    
