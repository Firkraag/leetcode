#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        cows = 0
        d = dict()
        for s in secret:
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                d[secret[i]] -= 1
        for i in range(len(secret)):
            if secret[i] != guess[i] and guess[i] in d and d[guess[i]] > 0:
                d[guess[i]] -= 1
                cows += 1
        return str(bulls) + 'A' + str(cows) + 'B'
