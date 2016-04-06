#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        a = n
        b = n / 2
        while a == b * 2:
            a = b
            b = b / 2
        if a == 1:
            return True
        else:
            return False
