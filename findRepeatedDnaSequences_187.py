#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n < 10:
            return []
        d = dict()
        d['A'] = 0
        d['C'] = 1
        d['G'] = 2
        d['T'] = 3
        
        codes = [0] * (n - 10 + 1)
        code = 0
        for i in range(10):
            code += d[s[i]] * (4 ** i)
        codes[0] = code
        constant = 4 ** 9
        for i in range(1, n - 10 + 1):
            codes[i] = (codes[i - 1] - d[s[i - 1]]) / 4 + d[s[i + 9]] * constant
        times = dict()
        for i in range(n - 10 + 1):
            if codes[i] in times:
                times[codes[i]][0] += 1
            else:
                l = [1, i]
                times[codes[i]] = l
        return [s[value[1] : value[1] + 10] for key, value in times.iteritems() if value[0] > 1]
        
