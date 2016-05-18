#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        solutions = set()
        solutions.add(tuple())
        partial = []
        self.backtracking(nums, 0, len(nums) - 1, partial, solutions)
        return [list(solution) for solution in solutions]
        
    def backtracking(self, nums, start, end, partial, solutions):
        if start > end:
            return
        self.backtracking(nums, start + 1, end, partial, solutions)
        partial.append(nums[start])
        solutions.add(tuple(partial[:]))
        self.backtracking(nums, start + 1, end, partial, solutions)
        partial.pop()
        
