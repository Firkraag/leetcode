class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = 10000
        c = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    c += 1
        print c