#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 0:
            return True
        jump = [False] * n
        jump[-1] = True
        for i in range(n - 2, -1, -1):
            step = nums[i]
            j = 1
            while j <= step and i + j <= n - 1:
                if jump[i + j]:
                    jump[i] = True
                    break
                else:
                    j += nums[i + j] + 1
        #print jump
        return jump[0]
