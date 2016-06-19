#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        l = [0] + sorted(citations)
        for h in range(n, 0, -1):
            if l[n - h] <= h and l[n - h + 1] >= h:
                return h
        return 0
        
