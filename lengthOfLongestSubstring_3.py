#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        index = dict()
        maximum = 0
        i = 0
        j = 0
        while j < n:
            if s[j] in index:
                i = max(i, index[s[j]])
            maximum = max(maximum, j - i + 1)
            index[s[j]] = j + 1
            j += 1
        return maximum
