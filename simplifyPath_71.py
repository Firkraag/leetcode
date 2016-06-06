#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if len(path) == 0:
            return '/'
        path = ['/'] + path.split('/')
        path.reverse()
        stack = []
        while len(path) != 0:
            string = path.pop()
            if string == '.' or string == '':
                pass
            elif string == '..':
                if stack[-1] == '/':
                    pass
                else:
                    stack.pop()
            else:
                stack.append(string)
        return stack[0] + '/'.join(stack[1:])
