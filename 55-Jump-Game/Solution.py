class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 0:
            return True
        lastTrue = n - 1
        for i in range(n - 2, -1, -1):
            step = nums[i]
            if i + step >= lastTrue:
                lastTrue = i
        return lastTrue == 0    
