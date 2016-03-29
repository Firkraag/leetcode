#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        position = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[position] = nums[i]
                position += 1
        for i in range(position, len(nums)):        
            nums[i] = 0
