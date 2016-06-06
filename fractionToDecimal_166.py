#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            return "NaN"
        elif numerator == 0:
            return "0"
        else:
            if (denominator < 0 and numerator > 0) or (denominator > 0 and numerator < 0):
                sign = "-"
            else:
                sign = ""
            numerator = abs(numerator)
            denominator = abs(denominator)
            integer = str(numerator / denominator)
            if numerator % denominator == 0:
                return sign + integer
            index = dict()
            decimal = list()
            i = self.fractionToDecimalAux(numerator % denominator, denominator, index, decimal, 0)
            if i == -1:
                return sign + integer + "." + ''.join(decimal)
            else:
                return sign + integer + "." + "".join(decimal[:i]) + '(' + "".join(decimal[i:]) + ")"
            
    def fractionToDecimalAux(self, numerator, denominator, index, decimal, i):
        if numerator in index:
            return index[numerator]
        elif numerator == 0:
            return -1
        else:
            index[numerator] = i
            numerator *= 10
            decimal.append(str(numerator / denominator))
            return self.fractionToDecimalAux(numerator % denominator, denominator, index, decimal, i + 1)
