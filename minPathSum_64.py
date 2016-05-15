#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        global height, width
        
        height = len(grid)
        if height == 0:
            return 0
        width = len(grid[0])
        if width == 0:
            return 0
        if height == 1 and width == 1:
            return grid[0][0]
        sums = [[None] * width for i in range(height)]
        sums[height - 1][width - 1] = grid[height - 1][width - 1]
        self.minPathSumAux(sums, 0, 0, grid)
        return sums[0][0]
        
    def minPathSumAux(self, sums, row, col, grid):
        global height, width
        
        sums[row][col] = float("Inf")
        if row + 1 < height:
            if sums[row + 1][col] == None:
                self.minPathSumAux(sums, row + 1, col, grid)
            sums[row][col] = min(sums[row + 1][col] + grid[row][col], sums[row][col])
        if col + 1 < width:
            if sums[row][col + 1] == None:
                self.minPathSumAux(sums, row, col + 1, grid)
            sums[row][col] = min(sums[row][col + 1] + grid[row][col], sums[row][col])
