#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return inorder_tree_walk(root.left, root.right)
        
def inorder_tree_walk(node1, node2):
    if node1 != None and node2 != None:
        if node1.val == node2.val:
            return inorder_tree_walk(node1.left, node2.right) and inorder_tree_walk(node1.right, node2.left)
        else:
            return False
    elif node1 != None and node2 == None:
        return False
    elif node1 == None and node2 != None:
        return False
    else:
        return True
        
