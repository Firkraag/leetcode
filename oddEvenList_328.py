#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        odd_list = ListNode(None)
        even_list = ListNode(None)
        head_odd = odd_list
        head_even = even_list
        even = False
        while node != None:
            if even:
                even_list.next = node
                even_list = node
                even = False
            else:
                odd_list.next = node
                odd_list = node
                even = True
            node = node.next
        odd_list.next = head_even.next
        even_list.next = None
        return head_odd.next
