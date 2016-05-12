#!/usr/bin/env python
# coding=utf-8
 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root != None:
            self.flatten_aux(root)
    
    def flatten_aux(self, node):
        if node.left == None and node.right == None:
            return node
        elif node.left == None and node.right != None:
            return self.flatten_aux(node.right)
        elif node.left != None and node.right == None:
            tail = self.flatten_aux(node.left)
            node.right = node.left
            node.left = None
            return tail
        else:
            tail1 = self.flatten_aux(node.left)
            tail2 = self.flatten_aux(node.right)
            tail1.left = None
            tail1.right = node.right
            node.right = node.left
            node.left = None
            return tail2
