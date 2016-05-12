#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total1 = (0 + n) * (n + 1) / 2
        total2 = sum(nums)
        return total1 - total2
