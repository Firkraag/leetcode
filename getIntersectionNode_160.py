#!/usr/bin/env python
# coding: utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        
        lenA = 0
        node = headA
        while node != None:
            lenA += 1
            node = node.next

        lenB = 0
        node = headB
        while node != None:
            lenB += 1
            node = node.next

        nodeA = headA
        nodeB = headB
        i = 0
        if lenA > lenB:
            while i < lenA - lenB:
                nodeA = nodeA.next
                i += 1
        else:
            while i < lenB - lenA:
                nodeB = nodeB.next
                i += 1
        intersection = None
        while nodeA != None:
            if nodeA.val == nodeB.val:
                if intersection == None:
                    intersection = nodeA
            else:
                intersection = None
            nodeA = nodeA.next
            nodeB = nodeB.next
        return intersection 
#def generateLinkedList(l):
 #   head = ListNode(None)
  #  node = head 
   # for i in l:
    #    node.next = ListNode(i)
     #   node = node.next
   # return head 

