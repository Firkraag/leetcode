#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1 = l1
        node2 = l2
        head = ListNode(None)
        node = head
        while node1 != None and node2 != None:
            if node1.val <= node2.val:
                node.next = node1
                node = node.next
                node.val = node1.val
                node1 = node1.next
            else:
                node.next = node2
                node = node.next
                node.val = node2.val
                node2 = node2.next
        if node1 == None:
            node.next = node2
        else:
            node.next = node1
        return head.next
        
