#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        l = [0] * 26
        group = []
        index = dict()
        for string in strs:
            for char in string:
                l[ord(char) - ord('a')] += 1
            key = tuple(l)
            if key in index:
                group[index[key]].append(string)
            else:
                group.append([])
                group[-1].append(string)
                index[key] = len(group) - 1
            for i in range(26):
                l[i] = 0
        return group
