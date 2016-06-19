#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = float("Inf")
        for num in nums:
            minimum = min(minimum, num)
        return minimum
