#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = head
        d = dict()
        length = 0
        if node == None:
            return None
        while node != None:
            length += 1
            d[length] = node
            node = node.next
        if n == length:
            first = d[1]
            return first.next
        elif n == 1:
            first = d[1]
            node = d[length - 1]
            node.next = None
            return first
        else:
            node = d[length + 1 - n]
            prev_node = d[length - n]
            prev_node.next = node.next
            first = d[1]
            return first
        
        
            
            
        
