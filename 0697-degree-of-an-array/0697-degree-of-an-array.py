class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = 1
        intervals = dict()
        smallest_length = 1
        for i, num in enumerate(nums):
            if num in intervals:
                intervals[num][2] = i
                intervals[num][0] += 1
                if intervals[num][0] > degree:
                    smallest_length = intervals[num][2] - intervals[num][1] + 1
                    degree = intervals[num][0]
                elif intervals[num][0] == degree:
                    smallest_length = min(smallest_length, intervals[num][2] - intervals[num][1] + 1)
            else:
                intervals[num] = [1, i, i]
        return smallest_length