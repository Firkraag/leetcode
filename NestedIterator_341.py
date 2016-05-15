#!/usr/bin/env python
# coding=utf-8
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        for v in nestedList:
            print type(v)
            if v.isInteger():
                print v.getInteger()
            else:
                print v.getList()
        self.container = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.container.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.container) == 0:
            return False
        if self.container[-1].isInteger():
            return True
        else:
            while len(self.container) != 0 and not self.container[-1].isInteger():
                nested_integer = self.container.pop()
                l = nested_integer.getList()
                if len(l) != 0:
                    self.container.extend(l[::-1])
            if len(self.container) == 0:
                return False
            else:
                return True
                
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
