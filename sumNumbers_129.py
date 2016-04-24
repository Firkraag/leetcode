#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global sum
        sum = 0
        if root == None:
            return 0
        inorder_tree_walk(root, 0)
        return sum
        
def inorder_tree_walk(node, path_sum):
    global sum
    if node.left == None and node.right == None:
        sum += (path_sum * 10 + node.val)
    if node.left != None:
        inorder_tree_walk(node.left, path_sum * 10 + node.val)
    if node.right != None:
        inorder_tree_walk(node.right, path_sum * 10 + node.val)
