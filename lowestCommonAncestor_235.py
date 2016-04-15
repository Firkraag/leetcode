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
        node = root
        p_ancestors = [root]
        while node != p:
            if node.val < p.val:
                node = node.right
            else:
                node = node.left
            p_ancestors.append(node)
        
        node = root
        q_ancestors = [root]
        while node != q:
            if node.val < q.val:
                node = node.right
            else:
                node = node.left
            q_ancestors.append(node)   
        
        n1 = len(p_ancestors)
        n2 = len(q_ancestors)
        i = 0
        j = 0
        while i < n1 and j < n2 and p_ancestors[i] == q_ancestors[j]:
            lca = p_ancestors[i]
            i += 1
            j += 1
        return lca
