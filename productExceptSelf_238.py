#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        elif n == 1:
            return [1]
        else:
            output = [0] * n
            self.productExceptSelfAux(nums, 0, n - 1, output)
            return output
            
    def productExceptSelfAux(self, nums, start, end, output):
        if start == end:
            output[start] = 1
            return nums[start]
        else:
            mid = (start + end) / 2
            product1 = self.productExceptSelfAux(nums, start, mid, output)
            product2 = self.productExceptSelfAux(nums, mid + 1, end, output)
            for i in range(start, mid + 1):
                output[i] *= product2
            for i in range(mid + 1, end + 1):
                output[i] *= product1
            return product1 * product2
