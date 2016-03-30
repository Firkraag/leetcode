#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k > n:
            k = k % n
        for i in range(1, k + 1):
            tmp = nums[n - k + i - 1]
            nums[i:n - k + i] = nums[i - 1:n - k + i - 1]
            nums[i - 1] = tmp
