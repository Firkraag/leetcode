#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        T = TreeNode(root.val)
        preorder_tree_walk(root, T)
        return T
        
def preorder_tree_walk(source, dest):
    if source != None:
        if source.left != None:
            dest.right = TreeNode(source.left.val)
            preorder_tree_walk(source.left, dest.right)
        if source.right != None:
            dest.left = TreeNode(source.right.val)
            preorder_tree_walk(source.right, dest.left)
