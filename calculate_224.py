#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, index = self.calculateAux(s, 0, len(s) - 1)
        return result
        
    def calculateAux(self, s, start, end):
        i = start
        result = None
        while i <= end:
            character = s[i]
            if character == '+' or character == '-':
                operator = character
                i += 1
            elif character == ' ':
                i += 1
            elif character == '(':
                value, i = self.calculateAux(s, i + 1, end)
                if result == None:
                    result = value
                else:
                    if operator == '+':
                        result += value
                    else:
                        result -= value
            elif character == ')':
                return result, i + 1
            else:
                start = i
                while i <= end and s[i].isdigit():
                    i += 1
                if result == None:
                    result = int(s[start:i])
                else:
                    value = int(s[start:i])
                    if operator == '+':
                        result += value
                    else:
                        result -= value
        return result, end + 1
        
