#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        global node_list
        node_list = []
        postorder_tree_walk(root)
        return node_list
        
def postorder_tree_walk(node):
    global node_list
    if node != None:
        postorder_tree_walk(node.left)
        postorder_tree_walk(node.right)
        node_list.append(node.val)
        
