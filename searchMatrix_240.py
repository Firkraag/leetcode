#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        for row in range(m):
            low = 0
            high = n - 1
            while low <= high:
                mid = (low + high) / 2
                if matrix[row][mid] == target:
                    return True
                elif target > matrix[row][mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
