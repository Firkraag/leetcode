#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = dict()
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        l = sorted(d.iteritems(), key = lambda pair: pair[1], reverse = True)
        return [l[i][0] for i in range(k)]
