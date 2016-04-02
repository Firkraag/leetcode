#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        low = 0
        high = n
        while low < high:
            mid = (low + high) / 2
            if target <= nums[mid]:
                high = mid
            else:
                low = mid + 1
        if high == n:
            return [-1, -1]
        elif nums[high] == target:
            left = high
            low = left
            high = n
            while low < high:
                mid = (low + high) / 2
                if target >= nums[mid]:
                    low = mid + 1
                else:
                    high = mid
            right = high - 1
            return [left, right]
        else:
            return [-1, -1]
