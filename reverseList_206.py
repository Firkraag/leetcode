#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pivot = head
        if pivot == None:
            return None
        elif pivot.next == None:
            return pivot
        head = pivot
        while pivot.next != None:
            node = pivot.next
            pivot.next = node.next
            node.next = head
            head = node
        return head
            
