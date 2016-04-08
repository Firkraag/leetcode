#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        node = head
        d = dict()
        length = 0
        while node != None:
            length += 1
            d[length] = node
            node = node.next
        left = 1
        right = length
        while right - left > 1:
            left_node = d[left]
            right_node = d[right]
            right_node.next = left_node.next
            left_node.next = right_node
            d[right - 1].next = None
            left += 1
            right -= 1
        
