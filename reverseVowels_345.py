#!/usr/bin/env python
# coding=utf-8
vowels = set('aeiouAEIOU')

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s) - 1
        l = list(s)
        while i < j:
            if isVowel(s[i]):
                while i < j and not isVowel(s[j]):
                    j -= 1
                l[i], l[j] = l[j], l[i]
                j -= 1
            i += 1
        return ''.join(l)
        
def isVowel(c):
    return c in vowels
        
                    
