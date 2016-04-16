#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1 = list(s)
        l1.sort()
        l2 = list(t)
        l2.sort()
        return l1 == l2
