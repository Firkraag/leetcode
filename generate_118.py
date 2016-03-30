#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        else:
            pascal_triangle = [None] * numRows
            pascal_triangle[0] = [1]
            pascal_triangle[1] = [1, 1]
            for i in range(2, numRows):
                pascal_triangle[i] = [None] * (i + 1)
                current_level = pascal_triangle[i]
                current_level[0] = 1
                current_level[i] = 1
                prev_level = pascal_triangle[i - 1]
                for j in range(1, i):
                    current_level[j] = prev_level[j - 1] + prev_level[j]
            return pascal_triangle
