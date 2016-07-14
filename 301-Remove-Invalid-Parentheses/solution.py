class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) == 0:
            return [""]
        from collections import deque
        result = []
        queue = deque()
        visited = set()
        queue.append(s)
        visited.add(s)
        length = None
        while len(queue) != 0:
            s = queue.popleft()
            if length != None:
                if len(s) == length and self.isValid(s):
                    result.append(s)
            else:
                if self.isValid(s):
                    result.append(s)
                    length = len(s)
                else:
                    for i in range(len(s)):
                        string = s[:i] + s[i + 1:]
                        if string not in visited: 
                            queue.append(string)
                            visited.add(string)
        return result
    
    def isValid(self, s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                if count == 0:
                    return False
                else:
                    count -= 1
        return count == 0
