#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = 0
        integer = 0
        while i < n:
            if s[i] == 'M':
                integer += 1000
                i += 1
            elif s[i] == 'D':
                integer += 500
                i += 1
            elif s[i] == 'C':
                if i + 1 < n and s[i + 1] == 'D':
                    integer += 400
                    i += 2
                elif i + 1 < n and s[i + 1] == 'M':
                    integer += 900
                    i += 2
                else:
                    integer += 100
                    i += 1
            elif s[i] == 'L':
                integer += 50
                i += 1
            elif s[i] == 'X':
                if i + 1 < n and s[i + 1] == 'L':
                    integer += 40
                    i += 2
                elif i + 1 < n and s[i + 1] == 'C':
                    integer += 90
                    i += 2
                else:
                    integer += 10
                    i += 1
            elif s[i] == 'V':
                integer += 5
                i += 1
            else:
                if i + 1 < n and s[i + 1] == 'V':
                    integer += 4
                    i += 2
                elif i + 1 < n and s[i + 1] == 'X':
                    integer += 9
                    i += 2
                else:
                    integer += 1
                    i += 1
        return integer
