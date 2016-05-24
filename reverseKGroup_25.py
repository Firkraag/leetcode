#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node = head
        count = 0
        ret = head
        prevLast = None
        while node != None:
            count += 1
            if count == k:
                ret = node
            if count % k == 0:
                tmp = node
                node = node.next
                tmp.next = None
                newHead = self.reverseList(head)
                if prevLast != None:
                    prevLast.next = newHead
                head.next = node
                prevLast = head
                head = node
            else:
                node = node.next
        return ret
            
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pivot = head
        if pivot == None:
            return None
        elif pivot.next == None:
            return pivot
        head = pivot
        while pivot.next != None:
            node = pivot.next
            pivot.next = node.next
            node.next = head
            head = node
        return head
