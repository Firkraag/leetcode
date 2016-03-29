class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        s = set()
        n = len(nums)
        A = sorted(nums)
        
        for l in range(n - 3):
            for i in range(l + 1, n - 2):
                j = i + 1
                k = n - 1
                while k > j:
                    value = A[l] + A[i] + A[j] + A[k]
                    if value == target:
                        s.add((A[l], A[i], A[j], A[k]))
                        j = j + 1
                        k = k - 1
                        while j < n and A[j] == A[j - 1]:
                            j = j + 1
                        while k >= 0 and A[k] == A[k + 1]:
                            k = k - 1
                    elif value > target:
                        k = k - 1
                    else:
                        j = j + 1
        return [list(element) for element in s]   
