#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        amount = dict()
        return self.robAux(root, amount)
        
    def robAux(self, node, amount):
        if node == None:
            return 0
        elif node in amount:
            return amount[node]
        value1 = node.val
        if node.left != None:
            value1 += self.robAux(node.left.left, amount) + self.robAux(node.left.right, amount)
        if node.right != None:
            value1 += self.robAux(node.right.left, amount) + self.robAux(node.right.right, amount)
        value2 = self.robAux(node.left, amount) + self.robAux(node.right, amount)
        amount[node] = max(value1, value2)
        return amount[node]
