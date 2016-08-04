class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = nums[:]
        l.sort()
        largerLength = n / 2
        smallerLength = n - largerLength
        nums[0:n:2] = l[smallerLength - 1::-1]
        nums[1:n:2] = l[n - 1:smallerLength - 1:-1]
        