#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            value = num % 9
            if value == 0:
                return 9
            else:
                return value
