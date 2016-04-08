#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        l = []
        while node != None:
            l.append(node.val)
            node = node.next
        l.sort()
        head = ListNode(None)
        prev_node = head
        for x in l:
            prev_node.next = ListNode(x)
            prev_node = prev_node.next
        return head.next
