#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        d = dict()
        length = 0
        node = head
        while node != None:
            length += 1
            d[length] = node
            node = node.next
        k = k % length
        if k == 0:
            return head
        node = d[length + 1 - k]
        prev_node = d[length - k]
        prev_node.next = None
        tail = d[length]
        tail.next = head
        return node
        
