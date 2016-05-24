#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        import string
        alphabet = string.ascii_uppercase
        d = dict()
        for i in range(1, 27):
            d[i] = alphabet[i - 1]
        title = []
        while n > 0:
            m = (n - 1) / 26
            reminder = n - m * 26
            title.insert(0, d[reminder])
            n = m
        return ''.join(title)
