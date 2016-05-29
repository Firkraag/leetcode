#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 3:
            return False
        single = nums[0]
        double = None
        for i in range(1, n):
            if double == None:
                if single < nums[i]:
                    double = (single, nums[i])
            else:
                if nums[i] > double[1]:
                    return True
                elif double[1] > nums[i] and nums[i] > single:
                    double = (single, nums[i])
            single = min(single, nums[i])
        return False       
        
