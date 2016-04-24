#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global min_depth
        min_depth = float("Inf")
        if root == None:
            return 0
        inorder_tree_walk(root, 0)
        return min_depth
        
def inorder_tree_walk(node, depth):
    global min_depth
    depth += 1
    if node.left == None and node.right == None:
        if depth < min_depth:
            min_depth = depth
    if node.left != None:
        inorder_tree_walk(node.left, depth)
    if node.right != None:
        inorder_tree_walk(node.right, depth)
