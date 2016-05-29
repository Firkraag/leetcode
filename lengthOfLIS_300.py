#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            if nums[0] < nums[1]:
                return 2
            else:
                return 1
        else:
            length = [0] * n
            length[0] = 1
            maximum = 1
            for i in range(1, n):
                l = [length[j] for j in range(i) if nums[j] < nums[i]]
                if len(l) == 0:
                    length[i] = 1
                else:
                    length[i] = max(l) + 1
                maximum = max(maximum, length[i])
            return maximum
