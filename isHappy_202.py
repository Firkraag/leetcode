#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        s.add(n)
        while True:
            l = decompose(n)
            n = square_sum(l)
            if n == 1:
                return True
            elif n in s:
                return False
            else:
                s.add(n)
                
def decompose(n):
    l = []
    while n > 0:
        l.append(n % 10)
        n /= 10
    return l

def square_sum(l):
    sum = 0
    for num in l:
        sum += num ** 2
    return sum
    
        
