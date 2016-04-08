#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        node = head
        list1 = ListNode(None)
        list2 = ListNode(None)
        head1 = list1
        head2 = list2
        while node != None:
            if node.val < x:
                list1.next = node
                list1 = node
            else:
                list2.next = node
                list2 = node
            node = node.next
        list1.next = head2.next
        list2.next = None
        return head1.next
                
        
