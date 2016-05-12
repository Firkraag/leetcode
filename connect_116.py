#!/usr/bin/env python
# coding=utf-8
# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root == None:
            return
        from collections import deque
        from collections import OrderedDict
        queue = deque([root])
        d = OrderedDict()
        root.level = 1
        while len(queue) != 0:
            node = queue.popleft()
            if node.left != None:
                node.left.level = node.level + 1   
                queue.append(node.left)
            if node.right != None:
                node.right.level = node.level + 1
                queue.append(node.right)
                
            if node.level not in d:
                d[node.level] = []
            d[node.level].append(node)
        l = [d[key] for key in d.iterkeys()]
        for i in range(len(l)):
            for j in range(len(l[i]) - 1):
                l[i][j].next = l[i][j + 1]
            l[i][-1].next = None
  
