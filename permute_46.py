#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = []
        partial = []
        self.backtracking(nums, permutations, partial)
        return permutations
        
    def backtracking(self, nums, permutations, partial):
        if len(nums) == 0:
            permutations.append(partial)
        else:
            for i in range(len(nums)):
                data = nums[:]
                partial2 = partial + [data.pop(i)]
                self.backtracking(data, permutations, partial2)
