#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split()
        if len(l) == 0:
            return 0
        else:
            return len(l[-1])
