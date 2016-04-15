#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        global node_list
        node_list = []
        preorder_tree_walk(root)
        return node_list
        
def preorder_tree_walk(node):
    global node_list
    if node != None:
        node_list.append(node.val)
        preorder_tree_walk(node.left)
        preorder_tree_walk(node.right)
