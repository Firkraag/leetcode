#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        ret = [[root.val]]
        reverse = True
        node_list = [root]
        while True:
            l = []
            while len(node_list) > 0:
                node = node_list.pop()
                if reverse:
                    if node.right != None:
                        l.append(node.right)
                    if node.left != None:
                        l.append(node.left)
                else:
                    if node.left != None:
                        l.append(node.left)
                    if node.right != None:    
                        l.append(node.right)
            reverse = not reverse
            if len(l) > 0:
                ret.append([node.val for node in l])
                node_list = l
            else:
                break
        return ret
                    
