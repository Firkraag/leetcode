#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        total = (C - A) * (D - B) + (G - E) * (H - F)
        if (A >= G or E >= C) or (B >= H or F >= D):
            return total
        l = [A, C, E, G]
        l.sort()
        width = l[2] - l[1]
        l = [B, D, F, H]
        l.sort()
        height = l[2] - l[1]
        return total - width * height
