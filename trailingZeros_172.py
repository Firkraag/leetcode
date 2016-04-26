#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        two_num = 0
        n1 = n
        while n1 >= 2:
            n1 /= 2
            two_num += n1
            
        five_num = 0
        n2 = n
        while n2 >= 5:
            n2 /= 5
            five_num += n2
        
        return min(two_num, five_num)
