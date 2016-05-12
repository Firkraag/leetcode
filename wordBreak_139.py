#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        length = len(s)
        m = [[False] * length for i in range(length)]
        for l in range(1, length + 1):
            for i in range(1, length - l + 2):
                j = i + l - 1
                for k in range(i, j):
                    if m[i - 1][k - 1] and m[k][j - 1]:
                        m[i - 1][j - 1] = True
                if not m[i - 1][j - 1]:
                    m[i - 1][j - 1] = self.judge(s[i - 1:j], wordDict)
        return m[0][length - 1]
            
    def judge(self, element, domain):
        return element in domain
        
