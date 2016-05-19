#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.buildSubTree(postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1)
        
    def buildSubTree(self, postorder, postStart, postEnd, inorder, inStart, inEnd):
        if postStart > postEnd or inStart > inEnd:
            return None
        else:
            val = postorder[postEnd]
            node = TreeNode(val)
            for index in range(inStart, inEnd + 1):
                if inorder[index] == val:
                    break
            sizeOfLeftSubTree = index - inStart
            sizeOfRightSubTree = inEnd - index
            node.left = self.buildSubTree(postorder, postStart, postStart + sizeOfLeftSubTree - 1, inorder, inStart, index - 1)
            node.right = self.buildSubTree(postorder, postEnd - sizeOfRightSubTree, postEnd - 1, inorder, index + 1, inEnd)
            return node
