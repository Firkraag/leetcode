class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        self.bucket(nums)
        #print nums
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
    
    def bucket(self, nums):
        n = len(nums)
        for i in range(n):
            #print i + 1
            index = nums[i] - 1
            while nums[i] != i + 1 and 0 <= index and index < n and index + 1 != nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                index = nums[i] - 1
                #print nums
