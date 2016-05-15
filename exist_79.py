#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        height = len(board)
        width = len(board[0])
        solutions = [[-1] * width for i in range(height)]
        for i in range(height):
            for j in range(width):
                if self.searchWord(board, word, i, j, solutions, 0):
                    return True
        return False
        
    def searchWord(self, board, word, row, col, solutions, index):
        if solutions[row][col] != -1 or board[row][col] != word[index]:
            return False
        solutions[row][col] = index
        if index == len(word) - 1:
            return True
        if col >= 1 and self.searchWord(board, word, row, col - 1, solutions, index + 1):
            return True
        if col < len(board[0]) - 1 and self.searchWord(board, word, row, col + 1, solutions, index + 1):
            return True
        if row >= 1 and self.searchWord(board, word, row - 1, col, solutions, index + 1):
            return True
        if row < len(board) - 1 and self.searchWord(board, word, row + 1, col, solutions, index + 1):
            return True
        solutions[row][col] = -1
        return False
        
