class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        elif n == 1:
            return nums
        nums.sort()
        length = [1] * n
        index = [-1] * n
        for i in range(1, n):
            maximum = 0
            idx = -1
            for j in range(i):
                if length[j] > maximum and nums[i] % nums[j] == 0:
                    maximum = length[j]
                    idx = j
            length[i] = maximum + 1
            index[i] = idx
        idx = length.index(max(length))
        ret = []
        while idx != -1:
            ret.append(nums[idx])
            idx = index[idx]
        return ret[::-1]
