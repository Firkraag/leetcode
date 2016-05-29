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
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if node.child[index] == None:
                return False
            else:
                node = node.child[index]
        return node.freq > 0

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if node.child[index] == None:
                return False
            else:
                node = node.child[index]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
