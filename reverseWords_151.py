#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s.isspace():
            return ""
        i = 0
        n = len(s)
        reverse = ""
        while i < n:
            original = i
            if s[i].isspace():
                while i < n and s[i].isspace():
                    i += 1
                reverse = " " + reverse
            else:
                while i < n and not s[i].isspace():
                    i += 1
                reverse = s[original:i] + reverse
        return reverse.lstrip().rstrip()  
