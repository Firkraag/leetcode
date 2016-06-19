#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        n = len(nums)
        t = nums[0]
        low = 0
        high = n
        while low < high:
            mid = (low + high) / 2
            if nums[mid] >= t:
                low = mid + 1
            else:
                high = mid
        pivot = high % n
        index = self.binarySearch(nums, target, 0, pivot - 1)
        if index == -1:
            return self.binarySearch(nums, target, pivot, n - 1)
        else:
            return index
    
    def binarySearch(self, nums, target, low, high):
        if low > high:
            return -1
        elif low == high:
            if nums[low] == target:
                return low
            else:
                return -1
        else:
            while low <= high:
                mid = (low + high) / 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
                    
