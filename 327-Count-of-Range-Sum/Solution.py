class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        global count
        count = 0
        n = len(nums)
        if n > 0:
            self.countRangeSumAux(nums, lower, upper, 0, n - 1)
        return count
        
    def countRangeSumAux(self, nums, lower, upper, left, right):
        global count
        if left == right:
            if lower <= nums[left] and nums[left] <= upper:
                count += 1
            return [nums[left]], [nums[right]]
        else:
            mid = (left + right) / 2
            forward1, backward1 = self.countRangeSumAux(nums, lower, upper, left, mid)
            forward2, backward2 = self.countRangeSumAux(nums, lower, upper, mid + 1, right)
            forward = forward1 + [forward1[-1] + value for value in forward2]
            backward = backward2 + [backward2[-1] + value for value in backward1]
            backward1.sort()
            forward2.sort()
            from bisect import bisect_left, bisect_right
            for value in backward1:
                index1 = bisect_left(forward2, lower - value)
                index2 = bisect_right(forward2, upper - value) - 1
                if index1 <= index2:
                    count += index2 - index1 + 1
            return forward, backward