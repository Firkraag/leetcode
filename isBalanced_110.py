#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        balanced, depth = tree_walk(root, 0)
        return balanced
def tree_walk(node, depth):
    if node != None:
        left_balanced, left_depth = tree_walk(node.left, depth + 1)
        right_balanced, right_depth = tree_walk(node.right, depth + 1)
        if left_balanced and right_balanced and abs(left_depth - right_depth) <= 1:
            return True, max(left_depth, right_depth)
        else:
            return False, None
    else:
        return True, depth
        
