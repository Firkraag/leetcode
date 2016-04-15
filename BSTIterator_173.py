#!/usr/bin/env python
# coding=utf-8
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.node_list = []
        self.inorder_tree_walk(root)
        self.index = 0
        self.length = len(self.node_list)
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < self.length
        
    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        return self.node_list[self.index - 1].val
        
    def inorder_tree_walk(self, node):
        if node != None:
            self.inorder_tree_walk(node.left)
            self.node_list.append(node)
            self.inorder_tree_walk(node.right)
            

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
