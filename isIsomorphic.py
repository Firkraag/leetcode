#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = dict()
        d2 = dict()
        n1 = len(s)
        n2 = len(t)
        if n1 != n2:
            return False
            
        for i in range(n1):
            if s[i] in d1:
                if d1[s[i]] != t[i]:
                    return False
            elif t[i] in d2:
                return False
            else:
                d1[s[i]] = t[i]
                d2[t[i]] = s[i]
        return True
