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
            dup_num = 1
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
                dup_num += 1
            if dup_num >= 2: 
                nums[position] = nums[i]
                nums[position + 1] = nums[i]
                position += 2
            else:
                nums[position] = nums[i]
                position += 1
            i += 1
        return position
