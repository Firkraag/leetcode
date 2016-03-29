class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        for s in range(0, n - m + 1):
            if haystack[s:s + m] == needle:
                return s
        return -1
