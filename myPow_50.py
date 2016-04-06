#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        elif n > 0:
            try:
                return pow(x, n)
            except OverflowError:
                return float("Inf")
        else:
            try:
                return 1.0 / pow(x, -n)
            except OverflowError:
                return 0.0
        
        
            
def pow(x, n):
    if n == 1:
        return x
    elif n % 2 == 0:
        return pow(x, n / 2) ** 2
    else:
        return pow(x, (n - 1) / 2) ** 2 * x
