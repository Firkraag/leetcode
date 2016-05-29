#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        l = sorted(citations)
        h = n
        while h > 0:
            start = n - 1 - h + 1
            if l[start] >= h and (start == 0 or l[start - 1] <= h):
                return h
            h -= 1
        return 0
