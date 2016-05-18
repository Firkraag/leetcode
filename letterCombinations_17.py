#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        partial = []
        solutions = []
        mappings = dict()
        pairs = [('0', ' '), ('1', '*'), ('2', 'abc'), ('3', 'def'), ('4', 'ghi'), ('5', 'jkl'), ('6', 'mno'), ('7', 'pqrs'), ('8', 'tuv'), ('9', 'wxyz')]
        for pair in pairs:
            mappings[pair[0]] = pair[1]
        self.backtracking(solutions, partial, 0, len(digits) - 1, mappings, digits)
        return solutions

    def backtracking(self, solutions, partial, start, end, mappings, digits):
        if start > end:
            solutions.append(''.join(partial))
            return
        string = mappings[digits[start]]
        for character in string:
            partial.append(character)
            self.backtracking(solutions, partial, start + 1, end, mappings, digits)
            partial.pop()
