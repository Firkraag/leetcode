#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = len(num1)
        n2 = len(num2)
        if n1 == 0 or n2 == 0:
            return "0"
        if n1 < n2:
            n1, n2 = n2, n1
            num1, num2 = num2, num1
        digits1 = [int(num1[i]) for i in range(n1 - 1, -1, -1)]
        digits2 = [int(num2[i]) for i in range(n2 - 1, -1, -1)]
        result = [0] * (n1 + n2)
        for j in range(n2):
            operand = digits2[j]
            start = j
            promote = 0
            if operand == 0:
                position = j
                continue
            for i in range(n1):
                position = start + i
                value = operand * digits1[i] + result[position] + promote
                result[position] = value % 10
                promote = value / 10
            if promote > 0:
                position += 1
                result[position] += promote
        return ''.join([str(result[i]) for i in range(position, -1, -1)])
    
