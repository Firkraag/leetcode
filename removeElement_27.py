#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        position = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[position], nums[i] = nums[i], nums[position]
                position += 1
        return position
