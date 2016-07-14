class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.remove(s, ans, 0, 0, ['(', ')'])
        return ans
        
    def remove(self, s, ans, last_i, last_j, par):
        stack = 0
        for i in range(last_i, len(s)):
            if s[i] == par[0]:
                stack += 1;
            elif s[i] == par[1]:
                stack -= 1
            if stack < 0:
                for j in range(last_j, i + 1):
                    if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):
                        self.remove(s[:j] + s[j + 1:], ans, i, j, par)
                return
        if par[0] == '(':
            self.remove(s[::-1], ans, 0, 0, [')', '('])
        else:
            ans.append(s[::-1])
