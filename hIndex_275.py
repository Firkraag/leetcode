#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        low = 0
        high = n + 1
        while low < high:
            h = (low + high) / 2
           # print low, high, h, citations[n - h], citations[n - h + 1]
            if n == h:
                value1 = 0
            else:
                value1 = citations[n - 1 - h]
                
            if h == 0:
                value2 = float("Inf")
            else:
                value2 = citations[n - h]
            
            if value1 <= h and value2 >= h:
                low = h + 1
            elif value1 > h:
                low = h + 1
            else:
                high = h
        return low - 1    
            
