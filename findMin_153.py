#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        target = nums[0]
        low = 0
        high = n
        while low < high:
            mid = (low + high) / 2
            if nums[mid] >= target:
                low = mid + 1
            elif nums[mid] < target:
                high = mid
        return nums[high % n]
        
