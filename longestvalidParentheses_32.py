#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        root = 0
        maximum = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(['(', i, 0])
            elif len(stack) != 0:
                p, index, number = stack.pop()
                if len(stack) != 0:
                    stack[-1][2] += i - index + 1
                    maximum = max(stack[-1][2], maximum)
                else:
                    root += i - index + 1
                    maximum = max(root, maximum)
            else:
                root = 0
        return maximum
                
