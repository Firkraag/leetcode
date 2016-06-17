#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        a, b = self.maxPathSumAux(root)
        return a
        
    def maxPathSumAux(self, root):
        if root.left == None and root.right == None:
            return root.val, root.val
        elif root.left == None and root.right != None:
            a, b = self.maxPathSumAux(root.right)
            return max(a, root.val, b + root.val), max(root.val, b + root.val)
        elif root.left != None and root.right == None:
            a, b = self.maxPathSumAux(root.left)
            return max(a, root.val, b + root.val), max(root.val, b + root.val)
        else:
            a1, b1 = self.maxPathSumAux(root.left)
            a2, b2 = self.maxPathSumAux(root.right)
            if b1 <= 0 and b2 <= 0:
                b = root.val
                a = max(a1, a2, b)
            elif b1 <= 0 and b2 > 0:
                b = root.val + b2
                a = max(a1, a2, b)
            elif b1 > 0 and b2 <= 0:
                b = root.val + b1
                a = max(a1, a2, b)
            else:
                b = max(b1, b2) + root.val
                a = max(a1, a2, root.val + b1 + b2)
            return a, b
