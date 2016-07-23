class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        length = 1
        status = 0
        for i in range(1, n):
            prevStatus = status
            if nums[i] > nums[i - 1]:
                status = 1
            elif nums[i] < nums[i - 1]:
                status = -1
            
            if prevStatus * status < 0:
                length += 1
        if status != 0:
            length += 1
        return length
        
