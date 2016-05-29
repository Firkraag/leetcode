#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1 + n2 != n3:
            return False
        elif n3 == 0:
            return True
        elif n1 == 0:
            return s2 == s3
        elif n2 == 0:
            return s1 == s3
        interleave = [[[None for k in range(n3)] for j in range(n2)] for i in range(n1)]
        return self.isInterleaveAux(s1, 0, n1 - 1, s2, 0, n2 - 1, s3, 0, n3 - 1, interleave)
        
    def isInterleaveAux(self, s1, start1, end1, s2, start2, end2, s3, start3, end3, interleave):
        if start1 > end1:
            return s2[start2:end2 + 1] == s3[start3 : end3 + 1]
        if start2 > end2:
            return s1[start1:end1 + 1] == s3[start3 : end3 + 1]
        if interleave[start1][start2][start3] != None:
            return interleave[start1][start2][start3]
        if s1[start1] == s3[start3]:
            if self.isInterleaveAux(s1, start1 + 1, end1, s2, start2, end2, s3, start3 + 1, end3, interleave):
                interleave[start1][start2][start3] = True
                return True
        if s2[start2] == s3[start3]:
            if self.isInterleaveAux(s1, start1, end1, s2, start2 + 1, end2, s3, start3 + 1, end3, interleave):
                interleave[start1][start2][start3] = True
                return True
        interleave[start1][start2][start3] = False
        return False
