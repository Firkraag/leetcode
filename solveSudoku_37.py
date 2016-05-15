#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row, col = self.findNext(board, 0, 0)
        self.solve(board, row, col)
        
    def solve(self, board, row, col):
        s = set([str(i) for i in range(1, 10)])
        for j in range(9):
            s.discard(board[row][j])
            s.discard(board[j][col])
        subRow = row / 3
        subCol = col / 3
        for i in range(subRow * 3, (subRow + 1) * 3):
            for j in range(subCol * 3, (subCol + 1) * 3):
                s.discard(board[i][j])
        if len(s) == 0:
            return False
        for num in s:
            board[row][col] = num
            pair = self.findNext(board, row, col)
            if pair == None:
                return True
            else:
                i = pair[0]
                j = pair[1]
                if self.solve(board, i, j):
                    return True
                else:
                    board[row][col] = '.'
                    
    def findNext(self, board, row, col):
        for i in range(col, 9):
            if board[row][i] == '.':
                return row, i
        
        for i in range(row + 1, 9):
            for j in range(9):
                if board[i][j] == '.':
                    return i, j
        return None
    
