#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        paths = []
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [str(root.val)]
        if root.left != None:
            inorder_tree_walk(root.left, paths, str(root.val))
        if root.right != None:
            inorder_tree_walk(root.right, paths, str(root.val))
        return paths
        
def inorder_tree_walk(node, paths, path):
    if node.left == None and node.right == None:
        paths.append(path + "->" + str(node.val))
    if node.left != None:
        inorder_tree_walk(node.left, paths, path + "->" + str(node.val))
    if node.right != None:
        inorder_tree_walk(node.right, paths, path + "->" + str(node.val))
