#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        d = dict()
        l = []
        for i in range(n):
            d[nums[i]] = 0
        for i in range(n):
            d[nums[i]] += 1
        for k, v in d.iteritems():
            if v == 1:
                l.append(k)
        return l
