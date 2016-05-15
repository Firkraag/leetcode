#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        elif n == 3:
            return max(nums)
        money = [[0] * n for i in range(n)]
        for i in range(n):
            money[i][i] = nums[i]
        for i in range(n - 1):
            money[i][i + 1] = max(nums[i], nums[i + 1])
        for length in range(3, n):
            for i in range(n - length + 1):
                money[i][i + length - 1] = max(nums[i] + money[i + 2][i + length - 1], money[i + 1][i + length - 1])
        money[0][n - 1] = max(nums[0] + money[2][n - 2], money[1][n - 1])
        return money[0][n - 1]
