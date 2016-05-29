#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #from tree to the diversion
        pAncestor = []
        qAncestor = []
        self.inorderTreeWalk(root, p, pAncestor)
        self.inorderTreeWalk(root, q, qAncestor)
        m = len(pAncestor)
        n = len(qAncestor)
        minimum = min(m, n)
        i = 0
        while i < minimum:
            if pAncestor[i] == qAncestor[i]:
                i += 1
            else:
                break
        return pAncestor[i - 1]

    def inorderTreeWalk(self, node, target, traverse):
        if target == node:
            traverse.append(node)
            return True
        traverse.append(node)
        if node.left != None:
            if self.inorderTreeWalk(node.left, target, traverse):
                return True
        if node.right != None:
            if self.inorderTreeWalk(node.right, target, traverse):
                return True
        traverse.pop()
        return False
