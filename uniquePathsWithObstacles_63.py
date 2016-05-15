#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        global height, width
        
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        if obstacleGrid[height - 1][width - 1] == 1:
            return 0
        if height == 1 and width == 1:
            return 1
        paths = [[None] * width for i in range(height)]
        paths[height - 1][width - 1] = 1
        self.uniquePathsAux(paths, 0, 0, obstacleGrid)
        return paths[0][0]
        
    def uniquePathsAux(self, paths, row, col, grid):
        global height, width
        
        paths[row][col] = 0
        if row + 1 < height and grid[row + 1][col] == 0:
            if paths[row + 1][col] == None:
                self.uniquePathsAux(paths, row + 1, col, grid)
            paths[row][col] += paths[row + 1][col]
        if col + 1 < width and grid[row][col + 1] == 0:
            if paths[row][col + 1] == None:
                self.uniquePathsAux(paths, row, col + 1, grid)
            paths[row][col] += paths[row][col + 1]
        
