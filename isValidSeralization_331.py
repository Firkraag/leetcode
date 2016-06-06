#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        string = preorder.split(",")
        boolean, index = self.isValid(string, 0, len(string) - 1)
        return boolean and index >= len(string)
        
    def isValid(self, string, start, end):
        if start > end:
            return False, 0
        root = string[start]
        if root == '#':
            return True, start + 1
        else:
            boolean, index = self.isValid(string, start + 1, end)
            if boolean:
                return self.isValid(string, index, end)
            else:
                return False, index
                
        
