#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        solutions = []
        partial = []
        valid = []
        self.backtracking(solutions, partial, valid, n, n)
        return solutions
        
    def backtracking(self, solutions, partial, valid, leftNum, rightNum):
        if leftNum == 0 and rightNum == 0:
            solutions.append(''.join(partial))
            return
        
        if leftNum > 0:
            partial.append('(')
            valid.append('(')
            self.backtracking(solutions, partial, valid, leftNum - 1, rightNum)
            partial.pop()
            valid.pop()
        if rightNum > 0 and self.isValid(valid):
            partial.append(')')
            self.backtracking(solutions, partial, valid, leftNum, rightNum - 1)
            partial.pop()
            valid.append('(')
            
    def isValid(self, valid):
        if len(valid) == 0:
            return False
        c = valid.pop()
        return c == '('
            
