#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x + 1
        while low < high:
            mid = (low + high) / 2
            if mid ** 2 <=  x:
                low = mid + 1
            else:
                high = mid
        return high - 1
            
        
