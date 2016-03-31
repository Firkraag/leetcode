#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row_status = [False] * m
        col_status = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_status[i] = True
                    col_status[j] = True
        for i in range(m):
            if row_status[i] == True:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n):
            if col_status[j] == True:
                for i in range(m):
                    matrix[i][j] = 0
