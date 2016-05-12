#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [0] * (n + 1)
        l[1] = 1
        l[2] = 1
        for i in range(3, n + 1):
            l[i] = max([max(l[j], j) * (i - j) for j in range(1, i)])
        
        return l[n]
            
