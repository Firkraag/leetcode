#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        reverse = 0
        for i in range(32):
            bit = n % 2
            n = n / 2
            reverse = reverse * 2 + bit
        return reverse
