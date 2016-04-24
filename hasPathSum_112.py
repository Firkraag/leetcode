#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        path_sum = 0
        if root == None:
            return False
        return inorder_tree_walk(root, path_sum, sum)
        
        
def inorder_tree_walk(node, path_sum, sum):
    if node.left == None and node.right == None:
        if path_sum + node.val == sum:
            return True
        else:
            return False
    if node.left != None:
        if inorder_tree_walk(node.left, path_sum + node.val, sum):
            return True
    if node.right != None:
        if inorder_tree_walk(node.right, path_sum + node.val, sum):
            return True
    return False
