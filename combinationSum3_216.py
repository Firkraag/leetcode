#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k < 1 or n < 1:
            return []
        elif k == 1:
            return [[n]]
        if k >= n or k * 9 <= n:
            return []
        solutions = []
        partial = []
        self.backtracking(solutions, partial, k, n, 1)
        return solutions
        
    def backtracking(self, solutions, partial, k, n, number):
        if n == 0 and k == 0:
            solutions.append(partial[:])
            return
        elif n == 0 and k > 0:
            return
        elif n > 0 and k == 0:
            return
        elif number > 9 or number > n:
            return
        else:
            partial.append(number)
            self.backtracking(solutions, partial, k - 1, n - number, number + 1)
            partial.pop()
            self.backtracking(solutions, partial, k, n, number + 1)
