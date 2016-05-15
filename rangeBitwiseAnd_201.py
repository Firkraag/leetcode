#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        elif m == n:
            return m
        ret = 0
        from math import log, floor
        logM = int(floor(log(m, 2)))
        logN = int(floor(log(n, 2)))
        if logM == logN:
            m = m - 2 ** logM
            n = n - 2 ** logN
            ret = ret + 2 ** logN + self.rangeBitwiseAnd(m, n)
        return ret
