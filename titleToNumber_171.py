#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        import string
        uppers = string.ascii_uppercase
        lowers = string.ascii_lowercase
        d = dict()
        i = 1
        for lower, upper in zip(lowers, uppers):
            d[lower] = i
            d[upper] = i
            i += 1
        value = 0
        for i in range(n):
            value += d[s[i]] * 26 ** (n - i - 1)
        return value
