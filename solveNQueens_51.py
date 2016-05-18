#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.'] * n for i in range(n)]
        solutions = []
        placeQueen(board, n, 0, solutions)
        return solutions

def placeQueen(board, row_size, queen, solutions):
    n = len(board[0])
    if queen == n:
        solutions.append([''.join(board[row]) for row in range(len(board))])     
        return
    for j in range(row_size):
        if canPlace(board, j, queen):
            board[j][queen] = 'Q'
            placeQueen(board, row_size, queen + 1, solutions)
            board[j][queen] = '.'

def canPlace(board, row, queen):
    n = len(board[0])
    if col_verify(board, n, queen) and row_verify(board, row, n) and diagnoal_verify(board, row, queen):
        return True
    else:
        return False
        
def col_verify(board, row_size, col):
    for i in range(row_size):
        if board[i][col] == 'Q':
            return False
    return True
    
def row_verify(board, row, col_size):
    for j in range(col_size):
        if board[row][j] == 'Q':
            return False
    return True
    
def diagnoal_verify(board, row, col):
    i = row
    j = col
    n = len(board[0])
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while i < n and j < n:
        if board[i][j] == 'Q':
            return False
        i += 1
        j += 1
    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1
    i = row
    j = col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    return True
