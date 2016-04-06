#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        if node == None:
            return None
        elif node.next == None:
            return node
        prev_node = node
        node = node.next
        while node != None:
            if node.val == prev_node.val:
                prev_node.next = node.next
            else:
                prev_node = node
            node = node.next
        return head
