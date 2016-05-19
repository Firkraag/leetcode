#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1
        elif n == 1:
            if nums[0] == 0:
                return 0
            else:
                return -1
        return self.findDuplicateAux(nums, 1, n - 1)
        
    def findDuplicateAux(self, nums, low, high):
        if low == high:
            return low
        else:
            mid = (low + high) / 2
            sizeFirst = mid - low + 1
            sizeSecond = high - mid
            first = 0
            second = 0
            for num in nums:
                if low <= num and num <= mid:
                    first += 1
                elif mid < num and num <= high:
                    second += 1
            if first > sizeFirst:
                return self.findDuplicateAux(nums, low, mid)
            else:
                return self.findDuplicateAux(nums, mid + 1, high)
