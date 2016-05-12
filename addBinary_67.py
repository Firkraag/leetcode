#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n1 = len(a)
        n2 = len(b)
        n = max(n1, n2)
        if n1 > n2:
            b = "0" * (n1 - n2) + b
        elif n1 < n2:
            a = "0" * (n2 - n1) + a
        c = [0] * (n + 1)
        promote = 0
        for i in range(n - 1, -1, -1):
            result = int(a[i]) + int(b[i]) + promote
            if result >= 2:
                promote = 1
                c[i + 1] = str(result - 2)
            else:
                promote = 0
                c[i + 1] = str(result)
        c[0] = str(promote)
        if c[0] == '1':
            return reduce(lambda x, y: x + y, c)
        else:
            return reduce(lambda x, y: x + y, c[1:])
        
            
