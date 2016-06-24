#!/usr/bin/env python
# coding=utf-8
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        if m == 0:
            self.size = 0
        else:
            n = len(matrix[0])
            if n == 0:
                self.size = 0
            else:
                self.size = m * n
                self._computeSum(matrix)

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.size == 0:
            return 0
        else:
            return self.sum[row2 + 1][col2 + 1] - self.sum[row1][col2 + 1] - self.sum[row2 + 1][col1] + self.sum[row1][col1]
        
    # compute the sum of elements inside the rectangle whose upper left corner is the first element     
    def _computeSum(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        self.sum = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m + 1):
            self.sum[i][0] = 0
        for j in range(n + 1):
            self.sum[0][j] = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.sum[i][j] = self.sum[i - 1][j] + self.sum[i][j - 1] - self.sum[i - 1][j - 1] + matrix[i - 1][j - 1]


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
