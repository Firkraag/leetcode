#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        if target < candidates[0]:
            return []
        elif target == candidates[0]:
            return [[target]]
        solutions = []
        partial = []
        d = dict()
        for candidate in candidates:
            if candidate in d:
                d[candidate] += 1
            else:
                d[candidate] = 1
        data = sorted(d.iteritems(), key = lambda pair: pair[0])
        self.backtracking(solutions, partial, data, target, 0, len(data) - 1)
        return solutions
    
    def backtracking(self, solutions, partial, data, target, start, end):
        if target == 0:
            solutions.append(partial[:])
            return
        elif start > end:
            return
        else:
            value = data[start][0]
            times = data[start][1]
            for i in range(0, times + 1):
                if value * i <= target:
                    partial.extend([value] * i)
                    self.backtracking(solutions, partial, data, target - value * i, start + 1, end)
                    for j in range(1, i + 1):
                        partial.pop()
                else:
                    break
