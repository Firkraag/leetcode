#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global max_depth
        
        if root == None:
            return 0
        max_depth = 0
        inorder_tree_walk(root, 0)
        return max_depth

def inorder_tree_walk(node, depth):
    global max_depth
    
    if node.left == None and node.right == None:
        if max_depth < depth + 1:
            max_depth = depth + 1
    if node.left != None:
        inorder_tree_walk(node.left, depth + 1)
    if node.right != None:
        inorder_tree_walk(node.right, depth + 1)
        
