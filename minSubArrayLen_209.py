#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum = 0
        j = 0
        minimum = float("Inf")
        for i in range(n):
            while j < n and sum < s:
                sum += nums[j]
                j += 1
            if sum < s:
                break
            else:
                minimum = min(minimum, j - i)
                sum = sum - nums[i]
                
        if minimum == float("Inf"):
            return 0
        else:
            return minimum
