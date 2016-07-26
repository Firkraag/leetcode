class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        maximum = 0
        patches = 0
        i = 0
        while i < len(nums) and maximum < n:
            if maximum + 1 < nums[i]:
                maximum += maximum + 1
                patches += 1
            else:
                maximum += nums[i]
                i += 1
        if maximum < n:
            while maximum < n:
                maximum += maximum + 1
                patches += 1
        return patches