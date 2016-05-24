#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        split1 = version1.split('.')
        split2 = version2.split('.')
        n1 = len(split1)
        n2 = len(split2)
        i = 0
        while i < n1 and i < n2:
            num1 = int(split1[i])
            num2 = int(split2[i])
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
            else:
                i += 1
        if i == n1 and i == n2:
            return 0
        elif i == n1 and i < n2:
            while i < n2:
                num = int(split2[i])
                if num != 0:
                    return -1
                else:
                    i += 1
            return 0
        elif i < n1 and i == n2:
            while i < n1:
                num = int(split1[i])
                if num != 0:
                    return 1
                else:
                    i += 1
            return 0
