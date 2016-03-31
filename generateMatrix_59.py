#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        matrix = [[0] * n for i in xrange(n)]
        row_start = 0
        row_end = n - 1
        col_start = 0
        col_end = n - 1
        value = 1
        print matrix
        while row_start <= row_end and col_start <= col_end:
            print matrix
            if row_start == row_end:
                for i in range(col_start, col_end + 1):
                    matrix[row_start][i] = value
                    value += 1
            elif col_start == col_end:
                for i in range(row_start, row_end + 1):
                    matrix[i][col_end] = value
                    value += 1
            else:
                print matrix
                for i in range(col_start, col_end + 1):
                    print matrix[row_start]
                    print matrix[row_start][i]
                    matrix[row_start][i] = value
                    value += 1
                    print "result: ", matrix
                print matrix
                for i in range(row_start + 1, row_end + 1):
                    matrix[i][col_end] = value
                    value += 1
                print matrix
                for i in range(col_end - 1, col_start - 1, -1):
                    matrix[row_end][i] = value
                    value += 1
                print matrix
                for i in range(row_end - 1, row_start, -1):
                    matrix[i][col_start] = value
                    value += 1
                print matrix
            row_start += 1
            row_end -= 1
            col_start += 1
            col_end -= 1
        return matrix
