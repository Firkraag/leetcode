#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        n = len(nums)
        while i <= n - 1:
            count = 1
            while i < n - 1 and nums[i] == nums[i + 1]:
                count += 1
                i += 1
            if count > n / 2:
                return nums[i]
            else:
                i += 1
