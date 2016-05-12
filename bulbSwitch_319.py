#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt, ceil
        num = ceil(sqrt(n + 1))
        return (2* int(num) - 3) / 2 + 1
