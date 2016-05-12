#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        elif num == 1:
            return [0, 1]
        bits = [0] * (num + 1)
        bits[0] = 0
        bits[1] = 1
        from math import log, floor
        n = int(floor(log(num, 2)))
        for i in range(1, n):
            p = 2 ** i
            for j in range(p, 2 * p):
                bits[j] = bits[j - p] + 1
        p = 2 ** n
        for i in range(p, num + 1):
            bits[i] = bits[i - p] + 1
        return bits
