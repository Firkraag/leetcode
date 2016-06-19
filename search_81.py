#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        for num in nums:
            if target == num:
                return True
        return False
        
