#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n1 = len(s)
        n2 = len(t)
        if n1 < n2:
            return 0
        elif n1 == n2:
            if s == t:
                return 1
            else:
                return 0
        else:
            counts = [[0] * (n2 + 1) for i in range(n1 + 1)]
            counts[0][0] = 1
            for j in range(1, n2 + 1):
                counts[0][j] = 0
            for i in range(1, n1 + 1):
                counts[i][0] = 1
            for i in range(1, n1 + 1):
                for j in range(1, n2 + 1):
                    if i < j:
                        counts[i][j] = 0
                    else:
                        counts[i][j] = counts[i - 1][j]
                        if s[i - 1] == t[j - 1]:
                            counts[i][j] += counts[i - 1][j - 1]
            return counts[n1][n2]
            
