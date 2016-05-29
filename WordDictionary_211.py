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
        self.indices = set()
        
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
                node.indices.add(index)
                node.child[index] = child
                node = child
            else:
                node = node.child[index]
        node.freq += 1
        
        
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.trie.insert(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        node = self.trie.root
        return self._search(word, 0, len(word) - 1, node)
        for char in word:
            if char == '.':
                return self.s
            else:
                index = ord(char) - ord('a')
                if node.child[index] == None:
                    return False
                else:
                    node = node.child[index]
        return node.freq > 0
        
    def _search(self, word, start, end, node):
        if start > end:
            return node.freq > 0
        char = word[start]
        if char == '.':
            for index in node.indices:
                if self._search(word, start + 1, end, node.child[index]):
                    return True
            return False
        else:
            index = ord(char) - ord('a')
            if node.child[index] == None:
                return False
            else:
                return self._search(word, start + 1, end, node.child[index])
# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
