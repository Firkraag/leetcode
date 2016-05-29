#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        global m, n
        X = word1
        Y = word2
        m = len(X)
        n = len(Y)
        if m == 0:
            return n
        elif n == 0:
            return m
        c = [[None] * n for i in range(m)]
        return self.memoized_edit_distance(X, 0, Y, 0, c)
    
    def memoized_edit_distance(self, X, i, Y, j, c):
        global m, n
        if j > n - 1:
            if i <= m - 1:
                return m - i
            else:
                return 0
        elif i > m - 1:
            return n - j
        elif c[i][j] != None:
            return c[i][j]
        else:
            minimum = float("Inf")
            if X[i] == Y[j]:
                minimum = min(minimum, self.memoized_edit_distance(X, i + 1, Y, j + 1, c))
            minimum = min(minimum, 1 + self.memoized_edit_distance(X,i + 1, Y, j + 1, c))
            minimum = min(minimum, 1 + self.memoized_edit_distance(X, i, Y, j + 1, c))
            minimum = min(minimum, 1 + self.memoized_edit_distance(X, i + 1, Y, j, c)) 
            c[i][j] = minimum
            return minimum

