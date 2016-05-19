#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        node = head
        while node != None:
            nums.append(node.val)
            node = node.next
        return self.BST(nums, 0, len(nums) - 1)
    
    def BST(self, nums, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        node = TreeNode(nums[mid])
        node.left = self.BST(nums, start, mid - 1)
        node.right = self.BST(nums, mid + 1, end)
        return node
