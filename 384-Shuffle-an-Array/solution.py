class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.nums = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        from random import randint
        n = len(self.nums)
        nums = self.nums[:]
        for i in range(0, n):
            j = randint(i, n - 1)
            nums[i], nums[j] = nums[j], nums[i]
        return nums



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
