#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [None] * n
        ugly[0] = 1
        #searched = [[False] * 3 for i in range(n)]
        index1 = 0
        index2 = 0
        index3 = 0
        i = 1
        while i < n:
            while True:
                value1 = 2 * ugly[index1]
                value2 = 3 * ugly[index2]
                value3 = 5 * ugly[index3]
                #print "value", value1, value2, value3
                if value1 <= value2 and value1 <= value3:
                    if value1 <= ugly[i - 1]:
                        index1 += 1
                    else:
                        ugly[i] = value1
                        index1 += 1
                        break
                elif value2 <= value1 and value2 <= value3:
                    if value2 <= ugly[i - 1]:
                        index2 += 1
                    else:
                        ugly[i] = value2
                        index2 += 1
                        break
                else:
                    if value3 <= ugly[i - 1]:
                        index3 += 1
                    else:
                        ugly[i] = value3
                        index3 += 1
                        break
            #print i + 1, ugly[i], index1 + 1, index2 + 1, index3 + 1
            i += 1
        return ugly[n - 1]
