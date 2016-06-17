#!/usr/bin/env python
# coding=utf-8
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None
        node = head
        d = dict()
        while node != None:
            newNode = RandomListNode(node.label)
            d[node] = newNode
            node = node.next
        node = head
        while node != None:
            #copy next property
            if node.next != None:
                d[node].next = d[node.next]
            else:
                d[node].next = None
            #copy random property    
            if node.random != None:
                d[node].random = d[node.random]
            else:
                d[node].random = None
                
            node = node.next
        return d[head]
       
