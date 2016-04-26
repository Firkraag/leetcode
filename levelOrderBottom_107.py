#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
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
                
            if node.level in d:
                d[node.level].append(node.val)
            else:
                d[node.level] = []
                d[node.level].append(node.val)
        l = [d[key] for key in d.iterkeys()]
        l.reverse()
        return l    
        
