#!/usr/bin/env python
# coding=utf-8
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.bis = [0] * (len(self.nums) + 1)
        self.maxIndex = 0
        self.buildBIS()
        self.maxIndex = len(self.nums)

    def buildBIS(self):
        for i in range(len(self.nums)):
            idx = i + 1
            r = idx & -idx
            self.bis[idx] = self.sumRange(idx - r, idx - 2) + self.nums[i]
                
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        tmp = val
        val = val - self.nums[i]
        idx = i + 1
        self.nums[i] = tmp
        while idx <= self.maxIndex:
            self.bis[idx] += val
            idx += (idx & -idx)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > j:
            return 0
        elif i == j:
            return self.nums[i]
        else:
            return self.readSum(j + 1) - self.readSum(i)
            
    def readSum(self, idx):
        sum = 0
        while idx > 0:
            sum += self.bis[idx]
            idx -= (idx & -idx)
        return sum
        


