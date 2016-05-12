#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        nums = [0] * (n + 1)
        nums[0] = 1
        nums[1] = 1
        nums[2] = 2
        for i in range(3, n + 1):
            num = 0
            for j in range(1, i + 1):
                num += nums[j - 1] * nums[i - j] 
            nums[i] = num
        return nums[n]
