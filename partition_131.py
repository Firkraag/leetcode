#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        partial = []
        solutions = []
        substring = []
        self.backtracking(solutions, partial, 0, len(s) - 1, s, substring)
        return solutions
        
    def backtracking(self, solutions, partial, start, end, s, substring):
        if start > end:
            solutions.append(partial[:])
            return
        substring.append(s[start])
        self.backtracking(solutions, partial, start + 1, end, s, substring)
        if self.isPalindrome(substring):
            partial.append(''.join(substring))
            del substring[:]
            self.backtracking(solutions, partial, start + 1, end, s, substring)
            substring.extend(list(partial.pop())
        substring.pop()
        
    def isPalindrome(self, string):
        i = 0
        j = len(string) - 1
        while i < j:
            if string[i] != string[j]:
                return False
        return True
        
