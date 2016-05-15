#!/usr/bin/env python
# coding=utf-8
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        if self.iterator.hasNext():
            self.empty = False
            self.buffer = self.iterator.next()
        else:
            self.buffer = None
            self.empty = True
            
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.buffer

    def next(self):
        """
        :rtype: int
        """
        ret = self.buffer
        if self.iterator.hasNext():
            self.empty = False
            self.buffer = self.iterator.next()
        else:
            self.buffer = None
            self.empty = True
        return ret
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return not self.empty

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
