#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n1 = len(s)
        n2 = len(p)
        match = [[None] * n2 for i in range(n1)] 
        return self.isMatchAux(s, 0, n1 - 1, p, 0, n2 - 1, match)
        
    def isMatchAux(self, s, start1, end1, p, start2, end2, match):
        if start1 > end1:
            if start2 > end2:
                return True
            else:
                for i in range(start2, end2 + 1):
                    if p[i] != '*':
                        return False
                return True
        elif start2 > end2:
            return False
        elif match[start1][start2] != None:
            return match[start1][start2]
        
        if p[start2] == '?':
            match[start1][start2] = self.isMatchAux(s, start1 + 1, end1, p, start2 + 1, end2, match)
            return match[start1][start2]
        elif p[start2] == '*':
            i = start1
            while i <= end1 + 1: 
                if self.isMatchAux(s, i, end1, p, start2 + 1, end2, match): 
                    match[start1][start2] = True
                    return True
                else:
                    i += 1
            match[start1][start2] = False
            return False
        else:
            if p[start2] == s[start1]:
                match[start1][start2] =  self.isMatchAux(s, start1 + 1, end1, p, start2 + 1, end2, match)
            else:
                match[start1][start2] = False
            return match[start1][start2]
        
