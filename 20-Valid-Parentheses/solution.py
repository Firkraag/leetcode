class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        stack = []
        d = {'[': ']', '{':'}', '(':')'}
        se = set('])}')
        for i in range(n - 1, -1, -1):
            if s[i] in se:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                else:
                    c = stack.pop()
                    if c != d[s[i]]:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
       
