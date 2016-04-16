#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return inorder_tree_walk(p, q)
        
def inorder_tree_walk(node1, node2):
    if node1 != None and node2 != None:
        if node1.val == node2.val:
            return inorder_tree_walk(node1.left, node2.left) and inorder_tree_walk(node1.right, node2.right)
        else:
            return False
    elif node1 != None and node2 == None:
        return False
    elif node1 == None and node2 != None:
        return False
    else:
        return True
        
        
