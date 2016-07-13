class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        if m > n:
            return -1
        elif m == 0:
            return 0
        p = self.computePrefixFunction(needle)
        q = 0
        for i in range(n):
            while q > 0 and needle[q] != haystack[i]:
                q = p[q - 1]
            if needle[q] == haystack[i]:
                q += 1
            if q == m:
                return i - m + 1
        return -1
        
    def computePrefixFunction(self, needle):
        m = len(needle)
        k = 0
        p = [0] * m
        for i in range(1, m):
            while k > 0 and needle[k] != needle[i]:
                k = p[k - 1]
            if needle[k] == needle[i]:
                k += 1
            p[i] = k
        return p