#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < 1 and k < 1:
            return []
        solutions = []
        partial = []
        digits = range(1, n + 1)
        self.backtracking(solutions, partial, k, digits, 0, n - 1)
        return solutions
    
    def backtracking(self, solutions, partial, k, digits, start, end):
        if k == 0:
            solutions.append(partial[:])
            return
        elif start > end:
            return
        partial.append(digits[start])
        self.backtracking(solutions, partial, k - 1, digits, start + 1, end)
        partial.pop()
        if start < end:
            self.backtracking(solutions, partial, k, digits, start + 1, end)
