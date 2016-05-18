#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n < 4:
            return []
        solutions = []
        partial = []
        self.backtracking(solutions, partial, 0, n - 1, s)
        return solutions
        
    def backtracking(self, solutions, partial, start, end, s):
        if len(partial) == 4 and start > end:
            solutions.append('.'.join(partial))
            return
        elif len(partial) == 4 and start <= end:
            return
        elif len(partial) < 4 and start > end:
            return
        partial.append(s[start])
        self.backtracking(solutions, partial, start + 1, end, s)
        partial.pop()
        if start + 1 <= end and s[start] != '0':
            partial.append(s[start:start + 2])
            self.backtracking(solutions, partial, start + 2, end, s)
            partial.pop()
        if start + 2 <= end:
            integer = int(s[start:start + 3])
            if 100 <= integer and integer <= 255:
                partial.append(s[start:start + 3])
                self.backtracking(solutions, partial, start + 3, end, s)
                partial.pop()
                
        
