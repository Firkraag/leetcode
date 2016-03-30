#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        if n == 0:
            return [1]
        result = [0] * n
        value = digits[n - 1] + 1
        if value == 10:
            promote = 1
            result[n - 1] = 0
        else:
            promote = 0
            result[n - 1] = value
        for i in range(len(digits) - 2, -1, -1):
            value =  digits[i] + promote
            if value == 10:
                promote = 1
                result[i] = 0
            else:
                promote = 0
                result[i] = value
        if promote == 1:
            result.insert(0, 1)
        return result
