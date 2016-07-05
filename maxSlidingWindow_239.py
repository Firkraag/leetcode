class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        n = len(nums)
        if n == 0:
            return []
        result = [0] * (n - k + 1)
        mapping = [None] * n
        import heapq
        h = []
        for i in range(k):
            l = [-nums[i], False]
            mapping[i] = l
            heapq.heappush(h, l)
        result[0] = -h[0][0]
        for i in range(k, n):
            mapping[i - k][1] = True
            l = [-nums[i], False]
            mapping[i] = l
            heapq.heappush(h, l)
            while h[0][1]:
                heapq.heappop(h)
            result[i - k + 1] = -h[0][0]
        return result
