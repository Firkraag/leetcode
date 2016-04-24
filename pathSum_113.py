#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        path_sum = 0
        paths = []
        if root == None:
            return []
        inorder_tree_walk(root, path_sum, sum, paths, [])
        return paths
        
def inorder_tree_walk(node, path_sum, sum, paths, path):
    if node.left == None and node.right == None:
        if path_sum + node.val == sum:
            paths.append(path + [node.val])
    if node.left != None:
        inorder_tree_walk(node.left, path_sum + node.val, sum, paths, path + [node.val])
    if node.right != None:
        inorder_tree_walk(node.right, path_sum + node.val, sum, paths, path + [node.val])
