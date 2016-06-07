#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.generateTreesAux(1, n)
        
    def generateTreesAux(self, start, end):
        if start > end:
            return []
        trees = []
        for i in range(start, end + 1):
            l1 = self.generateTreesAux(start, i - 1)
            l2 = self.generateTreesAux(i + 1, end)
            n1 = len(l1)
            n2 = len(l2)
            if n1 == 0 and n2 == 0:
                trees.append(TreeNode(i))
            elif n1 == 0 and n2 != 0:
                for j in range(n2):
                    node = TreeNode(i)
                    node.right = l2[j]
                    trees.append(node)
            elif n1 != 0 and n2 == 0:
                for j in range(n1):
                    node = TreeNode(i)
                    node.left = l1[j]
                    trees.append(node)
            else:
                for j in range(n1):
                    leftChild = l1[j]
                    for k in range(n2):
                        node = TreeNode(i)
                        node.left = leftChild
                        node.right = l2[k]
                        trees.append(node)
        return trees
