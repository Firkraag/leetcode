#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        global level
        level = 1
        l = []
        if root == None:
            return []
        root.level = 1
        self.rightOrderTraversal(root, l)
        return l
        
    def rightOrderTraversal(self, node, l):
        global level
        if node.level == level:
            l.append(node.val)
            level += 1
        if node.right != None:
            node.right.level = node.level + 1
            self.rightOrderTraversal(node.right, l)
        if node.left != None:
            node.left.level = node.level + 1
            self.rightOrderTraversal(node.left, l)
            
