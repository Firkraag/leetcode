#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return False
        valid = set("+-.e0123456789")
        split = s.split()
        if len(split) != 1:
            return False
        s = split[0]
        n = len(s)
        indexOfE = -1
        indexOfDot = -1
        numberOfE = 0
        numberOfDot = 0
        indexOfSign = -1
        numberOfSign = 0
        for i in range(n):
            c = s[i]
            if c not in valid:
                return False
            elif c == '.':
                indexOfDot = i
                numberOfDot += 1
            elif c == 'e' or c =='E':
                indexOfE = i
                numberOfE += 1
            elif c == '+' or c == '-':
                indexOfSign = i
                numberOfSign += 1
            
        if numberOfE > 1 or numberOfDot > 1:
            return False
        
        elif numberOfE == 1 and numberOfDot == 1:
            if indexOfDot > indexOfE:
                return False
            else:
                return self.isDecimal(s, 0, indexOfE - 1, indexOfDot) and self.isInteger(s, indexOfE + 1, n - 1)
        
        elif numberOfE == 1 and numberOfDot == 0:
            return self.isInteger(s, 0, indexOfE - 1) and self.isInteger(s, indexOfE + 1, n - 1)
            
        elif numberOfE == 0 and numberOfDot == 1:
            return self.isDecimal(s, 0, n - 1, indexOfDot)
        
        else:
            return self.isInteger(s, 0, n - 1)
    
    def isDecimal(self, s, start, end, indexOfDot):
        length1 = indexOfDot - start
        length2 = end - indexOfDot 
        
        if length1 == 0 and length2 == 0:
            return False
        elif length1 == 0 and length2 > 0:
            return self.noSign(s, indexOfDot + 1, end)
        elif length1 > 0 and length2 == 0:
            return self.isInteger(s, start, indexOfDot - 1)
        else:
            if self.noSign(s, indexOfDot + 1, end):
                if length1 == 1:
                    return True
                else:
                    return self.isInteger(s, start, indexOfDot - 1)
            else:
                return False
            
    def isInteger(self, s,start, end):
        if start > end:
            return False
        elif start == end:
            if s[start] == '+' or s[start] == '-':
                return False
            else:
                return True
        for i in range(start, end + 1):
            c = s[i]
            if c == '+' or c == '-':
                if i != start:
                    return False
            elif c.isdigit():
                pass
            else:
                return False
        return True
    
    def noSign(self, s, start, end):
        s = set(s[start : end + 1])
        if '+' in s or '-' in s:
            return False
        else:
            return True
    
