#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        d = dict()
        node = head
        length = 0
        if node == None or node.next == None:
            return True
        while node != None:
            length = length + 1
            d[length] = node
            node = node.next
        head = 1
        tail = length
        while head < tail:
            if d[head].val != d[tail].val:
                return False
            head += 1
            tail -= 1
        return True
        
