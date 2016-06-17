#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n >= 11:
            return 0
        elif n == 0:
            return 1
        elif n == 1:
            return 10
        else:
            counts = [None] * (n + 1)
            counts[0] = 1
            counts[1] = 10
            factorial = 9
            for i in range(2, n + 1):
                factorial *= (10 - i + 1)
                counts[i] = counts[i - 1] + factorial
            return counts[n]
