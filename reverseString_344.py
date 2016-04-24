#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        l.reverse()
        return ''.join(l)
