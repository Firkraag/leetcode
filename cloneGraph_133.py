#!/usr/bin/env python
# coding=utf-8
# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if node == None:
            return None
        source = UndirectedGraphNode(node.label)
        d = dict()
        d[node] = source
        from collections import deque
        q = deque()
        q.append(node)
        while len(q) != 0:
            u = q.popleft()
            for v in u.neighbors:
                if v not in d:
                    vertex = UndirectedGraphNode(v.label)
                    d[v] = vertex
                    d[u].neighbors.append(vertex)
                    q.append(v)
                else:
                    d[u].neighbors.append(d[v])
        return source
        
