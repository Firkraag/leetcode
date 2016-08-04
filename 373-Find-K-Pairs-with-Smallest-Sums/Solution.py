class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(nums1)
        n = len(nums2)
        pairs = []
        for i in range(min(m, k)):
            for j in range(min(n, k)):
                pairs.append((nums1[i], nums2[j]))
        pairs.sort(key = lambda pair: pair[0] + pair[1])
        return pairs[:k]
