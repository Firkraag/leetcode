#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        elif n <= 9:
            return 1
        digits = []
        m = n
        while m > 0:
            digits.append(m % 10)
            m /= 10
        weights = [0] * len(digits)
        weights[0] = 1
        weights[1] = 1
        count = 0
        for i in range(2, len(digits)):
            weights[i] = 10 * weights[i - 1] + 10 ** (i - 1)
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] == 0:
                continue
            elif digits[i] == 1:
                n = n - 10 ** i
                count += weights[i] + n + 1 
            else:
                n = n - digits[i] * 10 ** i
                count += digits[i] * weights[i] + 10 ** i
            print count
        if digits[0] != 0:
            count += 1
        return count
