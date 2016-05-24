#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maximum = 0
        n = len(height)
        a = 0
        b = n - 1
        while a < b:
            if height[a] <= height[b]:
                maximum = max(maximum, height[a] * (b - a))
                a += 1
            else:
                maximum = max(maximum, height[b] * (b - a))
                b -= 1
        return maximum
        
