#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        if head == None or head.next == None:
            return head
        node = head
        while node.next != None:
            if node.next.val >= node.val:
                node = node.next
            else:
                nodeNext = node.next
                node.next = nodeNext.next
                head = self.insertionFromHead(head, nodeNext)
        return head
        
    def insertionFromHead(self, head, node):
        if node.val <= head.val:
            node.next = head
            return node
        else:
            pivot = head
            while True:
                if pivot.val <= node.val and node.val <= pivot.next.val:
                    node.next = pivot.next
                    pivot.next = node
                    break
                else:
                    pivot = pivot.next
            return head
