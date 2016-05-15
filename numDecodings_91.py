#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        elif n == 1:
            if s == '0':
                return 0
            else:
                return 1
        nums = [None] * n
        m = int(s[-1])
        if m == 0:
            nums[-1] = 0
        else:
            nums[-1] = 1
        m = int(s[n - 2:n])
        if 0 <= m and m <= 9:
            nums[-2] = 0
        else:
            nums[-2] = 0
            if m >= 10 and m <= 26:
                nums[-2] = 1
            nums[-2] += nums[-1]
        if n == 2:
            return nums[0]
        for i in range(n - 3, -1, -1):
            m = int(s[i:i + 2])
            if 0 <= m and m <= 9:
                nums[i] = 0
            elif m == 10:
                nums[i] = nums[i + 2]
            elif m > 10 and m <= 19:
                nums[i] = nums[i + 1] + nums[i + 2]
            elif m == 20:
                nums[i] = nums[i + 2]
            elif m > 20 and m <= 26:
                nums[i] = nums[i + 1] + nums[i + 2]
            else:
                nums[i] = nums[i + 1]
        return nums[0]
            
   
        
