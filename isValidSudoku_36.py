#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in range(9):
            if not validRow(board, row):
                return False
        for col in range(9):
            if not validCol(board, col):
                return False
        for i in range(3):
            for j in range(3):
                if not validSubBoard(board, i, j):
                    return False
                    
        return True
        
def validRow(board, row):
    s = set()
    for i in range(9):
        c = board[row][i]
        if c != '.':
            if c in s:
                return False
            else:
                s.add(c)
    return True
    
def validCol(board, col):
    s = set()
    for i in range(9):
        c = board[i][col]
        if c != '.':
            if c in s:
                return False
            else:
                s.add(c)
    return True

def validSubBoard(board, row_span, col_span):
    s = set()
    for i in range(row_span * 3, (row_span + 1) * 3):
        for j in range(col_span * 3, (col_span + 1) * 3):
            c = board[i][j]
            if c != '.':
                if c in s:
                    return False
                else:
                    s.add(c)
    return True
    
