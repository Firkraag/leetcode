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
        palindrome = [[None] * len(s) for i in range(len(s))]
        self.backtracking(solutions, partial, 0, len(s) - 1, s, palindrome)
        return solutions
    
    def backtracking(self, solutions, partial, start, end, s, palindrome):
        if start > end:
            solutions.append(partial[:])
        else:
            for i in range(start, end + 1):
                if self.isPalindrome(s, start, i, palindrome):
                    partial.append(s[start : i + 1])
                    self.backtracking(solutions, partial, i + 1, end, s, palindrome)
                    partial.pop()

    def isPalindrome(self, s, start, end, palindrome):
        if palindrome[start][end] != None:
            return palindrome[start][end]
        else:
            a = start
            b = end
            while a < b:
                if s[a] != s[b]:
                    palindrome[start][end] = False
                    return False
                else:
                    a += 1
                    b -= 1
            palindrome[start][end] = True
            return True
