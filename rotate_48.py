#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        row_start = 0
        row_end = n - 1
        col_start = 0
        col_end = n - 1
        while row_start < row_end:
            for i in range(row_start, row_end):
                matrix[row_start][i], matrix[i][col_end], matrix[row_end][col_end - i + row_start], matrix[row_end - i +row_start][col_start] = matrix[row_end - i + row_start][col_start], matrix[row_start][i], matrix[i][col_end],matrix[row_end][col_end - i + row_start]
            row_start += 1
            row_end -= 1
            col_start += 1
            col_end -= 1
