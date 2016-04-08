#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        prev_distinct = None
        while node != None:
            duplicate = False
            while node.next != None and node.val == node.next.val:
                node = node.next
                duplicate = True
            if duplicate == True:
                if prev_distinct == None:
                    head = node.next
                else:
                    prev_distinct.next = node.next
                node = node.next
            else:
                prev_distinct = node
                node = node.next
        return head
        
