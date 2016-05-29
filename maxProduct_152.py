#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            product = [[0, 0, 0] for i in range(n)]
            if nums[0] >= 0:
                product[0][0] = nums[0]
                product[0][1] = None
                product[0][2] = nums[0]
            else:
                product[0][0] = None
                product[0][1] = nums[0]
                product[0][2] = nums[0]
            #print product[0]
            for j in range(1, n):
                self.updateBoundaryPosMax(j, nums, product)
                self.updateBoundaryNegMin(j, nums, product)
                self.updateMax(j, nums, product)
               # print product[j]
        return product[n - 1][2]
    
    def updateBoundaryPosMax(self, j, nums, product):
        if nums[j] > 0:
            if product[j - 1][0] == None:
                product[j][0] = nums[j]
            elif product[j - 1][0] == 0:
                product[j][0] = nums[j]
            else:
                product[j][0] = nums[j] * product[j - 1][0]
        elif nums[j] == 0:
            product[j][0] = 0
        else:
            if product[j - 1][1] == None:
                product[j][0] = None
            else:
                product[j][0] = product[j - 1][1] * nums[j]
    
    def updateBoundaryNegMin(self, j, nums, product):
        if nums[j] > 0:
            if product[j - 1][1] == None:
                product[j][1] = None
            else:
                product[j][1] = product[j - 1][1] * nums[j]
        elif nums[j] == 0:
            product[j][1] = None
        else:
            if product[j - 1][0] == None:
                product[j][1] = nums[j]
            elif product[j - 1][0] > 0:
                product[j][1] = product[j - 1][0] * nums[j]
            else:
                product[j][1] = nums[j]
    
    def updateMax(self, j, nums, product):
        if product[j][0] != None:
            product[j][2] = max(product[j - 1][2], product[j][0])
        else:
            product[j][2] = max(product[j - 1][2], product[j][1])
