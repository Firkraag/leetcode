#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        global height, width
        
        height = len(dungeon)
        if height == 0:
            return 1
        width = len(dungeon[0])
        if width == 0:
            return 1
        hps = [[None] * width for i in range(height)]
        value = dungeon[height - 1][width - 1]
        if value >= 0:
            hps[height - 1][width - 1] = 1
        else:
            hps[height - 1][width - 1] = abs(value) + 1
        if height == 1 and width == 1:
            return hps[0][0]
        self.calculateAux(hps, 0, 0, dungeon)
        print hps
        return hps[0][0]
        
    def calculateAux(self, hps, row, col, dungeon):
        global height, width
        
        if row + 1 < height and hps[row + 1][col] == None:
            self.calculateAux(hps, row + 1, col, dungeon)
        if col + 1 < width and hps[row][col + 1] == None:
            self.calculateAux(hps, row, col + 1, dungeon)
        if row + 1 >= height and col + 1 < width:
            hp = hps[row][col + 1]
        elif row + 1 < height and col + 1 >= width:
            hp = hps[row + 1][col]
        elif row + 1 < height and col + 1 < width:
            hp = min(hps[row + 1][col], hps[row][col + 1])
        hp2 = dungeon[row][col]
        if hp2 >= 0:
            if hp2 >= hp:
                hps[row][col] = 1
            else:
                hps[row][col] = hp - hp2
        else:
            hps[row][col] = hp - hp2
