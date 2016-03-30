#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            prev_level = [1, 1]
            for i in range(2, rowIndex + 1):
                current_level = [None] * (i + 1)
                current_level[0] = 1
                current_level[i] = 1
                for j in range(1, i):
                    current_level[j] = prev_level[j - 1] + prev_level[j]
                prev_level = current_level
            return current_level
