#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red_num = 0
        white_num = 0
        blue_num = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                red_num += 1
            elif nums[i] == 1:
                white_num += 1
            else:
                blue_num += 1
        nums[0:red_num] = [0] * red_num
        nums[red_num: red_num + white_num] = [1] * white_num
        nums[red_num + white_num : len(nums)] = [2] * blue_num 
