class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        A = sorted(nums)
        closest = float("Inf")
        n = len(A)
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while k > j:
                s = A[i] + A[j] + A[k]
                if abs(s - target) < abs(closest - target):
                    closest = s
                if s == target:
                    return target
                elif s > target:
                    k = k - 1
                else:
                    j = j + 1
        return closest
