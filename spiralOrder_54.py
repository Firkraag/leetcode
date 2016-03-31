#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        m = len(matrix)
        n = len(matrix[0])
        spiral = [None] * (m * n)
        row_start = 0
        row_end = m - 1
        col_start = 0
        col_end = n - 1
        position = 0
        while row_start <= row_end and col_start <= col_end:
            if row_start == row_end:
                for i in range(col_start, col_end + 1):
                    spiral[position] = matrix[row_start][i]
                    position += 1
            elif col_start == col_end:
                for i in range(row_start, row_end + 1):
                    spiral[position] = matrix[i][col_end]
                    position += 1
            else:
                for i in range(col_start, col_end + 1):
                    spiral[position] = matrix[row_start][i]
                    position += 1
                for i in range(row_start + 1, row_end + 1):
                    spiral[position] = matrix[i][col_end]
                    position += 1
                for i in range(col_end - 1, col_start - 1, -1):
                    spiral[position] = matrix[row_end][i]
                    position += 1
                for i in range(row_end - 1, row_start, -1):
                    spiral[position] = matrix[i][col_start]
                    position += 1
            row_start += 1
            row_end -= 1
            col_start += 1
            col_end -= 1
        return spiral
