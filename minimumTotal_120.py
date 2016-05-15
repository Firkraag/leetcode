#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        pathSum = [0] * n
        for i in range(n):
            pathSum[i] = triangle[-1][i]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                pathSum[j] = triangle[i][j] + min(pathSum[j], pathSum[j + 1])
        return pathSum[0]
                
