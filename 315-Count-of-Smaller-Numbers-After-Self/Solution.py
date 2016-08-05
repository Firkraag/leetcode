class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [(nums[i], i) for i in range(len(nums))]
        count = [0] * len(nums)
        self.countSmallerAux(nums, 0, len(nums) - 1, count)
        return count
        
    def countSmallerAux(self, nums, start, end, count):
        if start < end:
            mid = (start + end) / 2
            self.countSmallerAux(nums, start, mid, count)
            self.countSmallerAux(nums, mid + 1, end, count)
            print nums, count
            self.merge(nums, start, mid, end, count)
    
    def merge(self, nums, start, mid, end, count):
        n1 = mid - start + 1
        n2 = end - mid
        L = [0] * (n1 + 1)
        R = [0] * (n2 + 1)
        for i in range(0, n1):
            L[i] = nums[start + i]
        for j in range(0, n2):
            R[j] = nums[mid + j + 1]
        L[n1] = (float("Inf"), 0)
        R[n2] = (float("Inf"), 0)
        i = 0
        j = 0
        index = [0] * (n1 + 1)
        for k in range(start, end + 1):
            if L[i][0] <= R[j][0]:
                nums[k] = L[i]
                index[i] = k - start + 1
                i = i + 1
            else:
                nums[k] = R[j]
                j = j + 1
        for i in range(n1):
            count[L[i][1]] += index[i] - (i + 1)

