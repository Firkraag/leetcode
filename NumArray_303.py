#!/usr/bin/env python
# coding=utf-8
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        n = len(nums)
        self.sum = [None] * n
        summing = 0
        for i in range(n):
            summing += nums[i]
            self.sum[i] = summing
            
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int                                                        
        :rtype: int
        """
        if i == 0:
            return self.sum[j]
        else:
            return self.sum[j] - self.sum[i - 1]
            
