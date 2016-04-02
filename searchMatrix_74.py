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
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        low = 0
        high = m - 1
        row = None
        while low <= high:
            mid = (low + high) / 2
            if matrix[mid][0] <= target and target <= matrix[mid][n - 1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                low = mid + 1
        if row == None:
            return False
        else:
            array = matrix[row]
            low = 0
            high = n - 1
            while low <= high:
                mid = (low + high) /2 
                if array[mid] == target:
                    return True
                elif array[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return False
            
                    
