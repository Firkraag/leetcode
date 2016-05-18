#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n <= 0 or k <= 0:
            return ""
        from math import factorial, ceil
        solution = []
        digits = [str(i) for i in range(0, n + 1)]
        while n > 0:
            n1 = factorial(n)
            n2 = factorial(n - 1)
            index = int(ceil(1.0 * k / n2))
            solution.append(digits.pop(index))
            n -= 1
            k -= n2 * (index - 1)
        return ''.join(solution)
