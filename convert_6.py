#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        elif numRows == 2:
            return s[::2] + s[1::2]
        else:
            rows = []
            for i in range(numRows):
                rows.append([])
            rowIndex = 0
            reverse = False
            for i in range(len(s)):
                rows[rowIndex].append(s[i])
                if rowIndex == numRows - 1:
                    rowIndex -= 1
                    reverse = True
                elif rowIndex == 0:
                    rowIndex += 1
                    reverse = False
                elif reverse:
                    rowIndex -= 1
                else:
                    rowIndex += 1
            #print rows
            return "".join(["".join(row) for row in rows])
