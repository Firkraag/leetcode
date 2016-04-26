#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ""
        
        thousand = num / 1000
        s += 'M' * thousand
        
        num = num % 1000
        hundred = num / 100
        if hundred == 9:
            s += 'CM'
        elif hundred >= 5 and hundred < 9:
            s += ('D' + 'C' * (hundred - 5))
        elif hundred == 4:
            s += 'CD'
        else:
            s += 'C' * hundred
        
        num = num % 100
        ten = num / 10
        if ten == 9:
            s += 'XC'
        elif ten >= 5 and ten < 9:
            s += ('L' + 'X' * (ten - 5))
        elif ten == 4:
            s += 'XL'
        else:
            s += 'X' * ten
        
        one = num % 10
        if one == 9:
            s += 'IX'
        elif one >= 5 and one < 9:
            s += ('V' + 'I' * (one - 5))
        elif one == 4:
            s += 'IV'
        else:
            s += 'I' * one
            
        return s
        
