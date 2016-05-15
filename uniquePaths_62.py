#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        global height, width
        
        height = m
        width = n
        if m == 1 and n == 1:
            return 1
        paths = [[None] * n for i in range(m)]
        paths[m - 1][n - 1] = 1
        self.uniquePathsAux(paths, 0, 0)
        return paths[0][0]
        
    def uniquePathsAux(self, paths, row, col):
        global height, width
        
        paths[row][col] = 0
        if row + 1 < height:
            if paths[row + 1][col] == None:
                self.uniquePathsAux(paths, row + 1, col)
            paths[row][col] += paths[row + 1][col]
        if col + 1 < width:
            if paths[row][col + 1] == None:
                self.uniquePathsAux(paths, row, col + 1)
            paths[row][col] += paths[row][col + 1]
        
        
