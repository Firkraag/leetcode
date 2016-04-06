#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        node = head
        prev_node = None
        while node != None:
            if node.val == val:
                next_node = node.next
                if prev_node != None:
                    prev_node.next = next_node
                else:
                    head = node.next
                    prev_node = None
            else:
                prev_node = node
            node = node.next
        return head
                
                
                
            
