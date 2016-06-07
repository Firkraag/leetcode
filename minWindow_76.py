#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == 0 or len(t) == 0:
            return ""
        minimum = float("Inf")
        nums = dict()
        chars = set(t)
        from collections import Counter
        counter = Counter(t)
        for key in counter.iterkeys():
            nums[key] = 0
        n = len(s)
        j = 0
        for i in range(n):
            while len(chars) != 0 and j < n:
                if s[j] in nums:
                    nums[s[j]] += 1
                    if nums[s[j]] >= counter[s[j]]:
                        chars.discard(s[j])
                j += 1
            #print chars, i, j, minimum
            if len(chars) == 0:
                if j - i < minimum:
                    minimum = j - i
                    pair = (i, j - 1)
            else:
                break
            
            if s[i] in nums:
                nums[s[i]] -= 1
                if nums[s[i]] < counter[s[i]]:
                    chars.add(s[i])
        if minimum == float("Inf"):
            return ""
        else:
            return s[pair[0] : pair[1] + 1]
