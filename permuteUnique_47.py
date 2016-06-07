#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if len(nums) == 0:
            return []
        from collections import Counter
        c = Counter(nums)
        counter = list(c.iteritems())
        permutations = []
        partial = [0] * n
        indices = set(range(0, n))
        self.backtracking(permutations, partial, counter, 0, len(counter) - 1, indices)
        return permutations
        
    def backtracking(self, permutations, partial, counter, start, end, indices):
        if start > end:
            permutations.append(partial[:])
        else:
            value = counter[start][0]
            num = counter[start][1]
            combination = self.combine(indices, num)
            for positions in combination:
                for position in positions:
                    partial[position] = value
                    indices.discard(position)
                self.backtracking(permutations, partial, counter, start + 1, end, indices)
                for position in positions:
                    indices.add(position)
                    
    def combine(self, indices, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        n = len(indices)
        if n < 1 and k < 1:
            return []
        solutions = []
        partial = []
        digits = list(indices)
        self.combineAux(solutions, partial, k, digits, 0, n - 1)
        return solutions
        
    def combineAux(self, solutions, partial, k, digits, start, end):
        if k == 0:
            solutions.append(partial[:])
            return
        elif start > end:
            return
        partial.append(digits[start])
        self.combineAux(solutions, partial, k - 1, digits, start + 1, end)
        partial.pop()
        if start < end:
            self.combineAux(solutions, partial, k, digits, start + 1, end)
