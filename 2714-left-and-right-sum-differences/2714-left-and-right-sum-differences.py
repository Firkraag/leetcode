class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n
        for i in range(n - 1):
            left_sum[i + 1] = left_sum[i] + nums[i]
        for i in range(n - 2, -1, -1):
            right_sum[i] = right_sum[i + 1] + nums[i + 1]
        return [abs(left_sum[i] - right_sum[i]) for i in range(n)]
        