#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        if target < candidates[0]:
            return []
        solutions = []
        partial = []
        self.backtracking(solutions, partial, candidates, target, 0, len(candidates) - 1)
        return solutions
    
    def backtracking(self, solutions, partial, candidates, target, start, end):
        if target == 0:
            solutions.append(partial[:])
            return
        elif start > end:
            return
        else:
            times = 0
            value = candidates[start]
            values = value * times
            while values <= target:
                partial.extend([value] * times)
                self.backtracking(solutions, partial, candidates, target - value * times, start + 1, end)
                for j in range(1, times + 1):
                    partial.pop()
                times += 1
                values = value * times
