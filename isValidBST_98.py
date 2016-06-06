#!/usr/bin/env python
# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        valid, minimum, maximum = self.inorder_tree_walk(root)
        return valid
        
    def inorder_tree_walk(self, node):
        if node.left == None and node.right == None:
            return True, node.val, node.val
        elif node.left != None and node.right != None:
            if node.left.val < node.val and node.val < node.right.val:
                valid1, minimum1, maximum1 = self.inorder_tree_walk(node.left)
                valid2, minimum2, maximum2 = self.inorder_tree_walk(node.right)
                if valid1 and valid2 and maximum1 < node.val and minimum2 > node.val:
                    return True, minimum1, maximum2;
                else:
                    return False, 0, 0
            else:
                return False, 0, 0
        elif node.left != None and node.right == None:
            if node.left.val < node.val:
                valid, minimum, maximum = self.inorder_tree_walk(node.left)
                if valid and maximum < node.val:
                    return True, minimum, node.val
                else:
                    return False, 0, 0
            else:
                return False, 0, 0
        else:
            if node.right.val > node.val:
                valid, minimum, maximum = self.inorder_tree_walk(node.right)
                if valid and minimum > node.val:
                    return True, node.val,maximum
                else:
                    return False, 0, 0
            else:
                return False, 0, 0
