#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = nums[:]
        l.insert(0, float("-Inf"))
        l.append(float("-Inf"))
        for i in range(1, len(l) - 1):
            if l[i] > l[i - 1] and l[i] > l[i + 1]:
                return i - 1
        
