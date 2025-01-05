class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        occurences = [False] * (k + 1)
        count = 0
        for i, num in enumerate(reversed(nums), 1):
            if num <= k and not occurences[num]:
                count += 1
                if count == k:
                    return i
                occurences[num] = True
        return 0


        