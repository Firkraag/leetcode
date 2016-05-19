#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        elif n == 2:
            nums[0], nums[1] = nums[1], nums[0]
        else:
            if nums[n - 2] < nums[n - 1]:
                nums[n - 2], nums[n - 1] = nums[n - 1], nums[n - 2]
                return
            for i in range(n - 3, -1, -1):
                if nums[i] < nums[i + 1]:
                    for j in range(i + 1, n):
                        if nums[j] > nums[i] and ((j < n - 1 and nums[j + 1] <= nums[i]) or j == n - 1):
                            nums[i], nums[j] = nums[j], nums[i]
                            low = i + 1
                            high = n - 1
                            while low < high:
                                nums[low], nums[high] = nums[high], nums[low]
                                low += 1
                                high -= 1
                            return
            nums.reverse()
            
