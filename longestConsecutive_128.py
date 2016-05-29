#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(set(nums))
        n = len(nums)
        maximum = 1
        i = 0
        while i < n - 1:
            length = 1
            while i < n - 1 and nums[i + 1] - nums[i] == 1:
                i += 1
                length += 1
            i += 1
            maximum = max(maximum, length)
        return maximum
        
