#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        if num == 1:
            return True
        else:
            a = num
            b = num / 2
            while a == b * 2:
                a = b
                b = b / 2
            b = a / 3
            while a == b * 3:
                a = b
                b = b /3
            b = a / 5
            while a == b * 5:
                a = b
                b = b / 5
            if a != 1:
                return False
            else:
                return True
                
                
