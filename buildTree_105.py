#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.buildSubTree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
        
        
    def buildSubTree(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        if preStart > preEnd or inStart > inEnd:
            return None
        else:
            val = preorder[preStart]
            node = TreeNode(val)
            for index in range(inStart, inEnd + 1):
                if inorder[index] == val:
                    break
            sizeOfLeftSubTree = index - inStart
            sizeOfRightSubTree = inEnd - index
            node.left = self.buildSubTree(preorder, preStart + 1, preStart + sizeOfLeftSubTree, inorder, inStart, index - 1)
            node.right = self.buildSubTree(preorder, preEnd - sizeOfRightSubTree + 1, preEnd, inorder, index + 1, inEnd)
            return node
