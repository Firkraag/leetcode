#!/usr/bin/env python
# coding=utf-8
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = [None] * 26
        self.char = None
        self.freq = 0
        self.searched = False
        
class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if node.child[index] == None:
                child = TrieNode()
                child.char = char
                node.child[index] = child
                node = child
            else:
                node = node.child[index]
        node.freq += 1
        
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        global m, n
        m = len(board)
        n = len(board[0])
        solutions = []
        partial = []
        status = [[False] * n for i in range(m)]
        
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        for i in range(m):
            for j in range(n):
                self.search(board, i, j, trie.root, solutions, status, partial)
        return solutions
        
    def search(self, board, i, j, node, solutions, status, partial):
        global m, n
        if status[i][j]:
            return
        char = board[i][j]
        index = ord(char) - ord('a')
        if node.child[index] == None:
            return
        else:
            node = node.child[index]
            partial.append(char)
            status[i][j] = True
            if node.freq > 0 and node.searched == False:
                solutions.append(''.join(partial))
                node.searched = True
            if i > 0:
                self.search(board, i - 1, j, node, solutions, status, partial)
            if i < m - 1:
                self.search(board, i + 1, j, node, solutions, status, partial)
            if j > 0:
                self.search(board, i, j - 1, node, solutions, status, partial)
            if j < n - 1:
                self.search(board, i, j + 1, node, solutions, status, partial)
            status[i][j] = False
            partial.pop()
            
