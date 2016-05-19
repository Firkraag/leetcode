#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        global therhold
        
        solution = []
        n = len(nums)
        if n == 0:
            return []
        elif n == 1:
            return [nums[0]]
        therhold = n / 3
        minimum = min(nums)
        maximum = max(nums)
        self.majorityElementAux(nums, minimum, maximum, solution)
        return solution
        
    def majorityElementAux(self, nums, low, high, solution):
        global therhold
        
        if low == high:
            solution.append(low)
            return
        mid = (low + high) / 2
        left = 0
        right = 0
        for num in nums:
            if num <= mid and low <= num:
                left += 1
            elif num > mid and num <= high:
                right += 1
        if left > therhold:
            self.majorityElementAux(nums, low, mid, solution)
        if right > therhold:
            self.majorityElementAux(nums, mid + 1, high, solution)
        
        
