#!/usr/bin/env python
# coding=utf-8
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.number = 0
        self.map = dict()
        self.head = Node()
        self.tail = self.head

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.map:
            node = self.map[key]
            self.removeNode(node)
            self.insertToHead(node)
            return node.value
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.removeNode(node)
            self.insertToHead(node)
        else:
            if self.number == self.capacity:
                tail = self.tail
                self.removeNode(tail)
                self.insertToHead(Node(key, value))
            else:
                self.insertToHead(Node(key, value))
             
    def removeNode(self, node):
        self.number -= 1
        del self.map[node.key]
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        if nextNode != None:
            nextNode.prev = prevNode
        if self.head.next == node:
            self.head.next = nextNode
        if self.tail == node:
            self.tail = prevNode
    
    def insertToHead(self, node):
        self.number += 1
        self.map[node.key] = node
        nextNode = self.head.next
        self.head.next = node
        if nextNode != None:
            nextNode.prev = node
        node.prev = self.head
        node.next = nextNode
        if self.tail == self.head:
            self.tail = node
        
class Node(object):
    def __init__(self, key = None, value = None):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value
