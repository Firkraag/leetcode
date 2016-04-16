#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        length = min([len(s) for s in strs])
        common_prefix = ""
        for index in range(length):
            if isCommon(strs, index):
                common_prefix = common_prefix + strs[0][index]
            else:
                return common_prefix
        return common_prefix
        
def isCommon(strs, index):
    for i in range(len(strs) - 1):
        if strs[i][index] != strs[i + 1][index]:
            return False
    return True
        
