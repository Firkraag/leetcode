#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        position = 0
        while i < n:
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            nums[position] = nums[i]
            position += 1
            i += 1
        return position
