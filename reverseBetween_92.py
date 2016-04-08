#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        elif m == 1:
            pivot = head
            length = 1
            while length < n:
                node = pivot.next
                pivot.next = node.next
                node.next = head
                head = node
                length += 1
            return head
        else:
            node = head
            length = 1
            while length < m - 1:
                node = node.next
                length += 1
            node_m_1 = node
            node_m = node_m_1.next
            pivot = node_m
            length = m
            while length < n:
                node = pivot.next
                pivot.next = node.next
                node.next = node_m
                node_m = node
                node_m_1.next = node_m
                length += 1
            return head
            
        
