#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        first = head
        if first == None:
            return None
        second = first.next
        if second == None:
            return first
        head = second
        second = first.next
        first.next = second.next
        second.next = first
        prev = first
        first = first.next
        while True:
            if first == None or first.next == None:
                break
            else:
                second = first.next
                prev.next = second
                first.next = second.next
                second.next = first
                prev = first
                first = first.next
        return head
        
