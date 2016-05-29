#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        lower = string.ascii_lowercase
        mappings = dict()
        code = [0] * len(words)
        for i in range(26):
            mappings[lower[i]] = (1 << i)
        for i in range(len(words)):
            value = 0
            word = words[i]
            for j in range(len(word)):
                c = word[j]
                value |= mappings[c]
            code[i] = value
        maximum = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if (code[i] & code[j]) == 0:
                    maximum = max(maximum, len(words[i]) * len(words[j]))
        return maximum
        
        
