# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        n = len(intervals)
        if n == 0:
            return []
        intervals = sorted(intervals, key = lambda interval:interval.start)
        first = intervals[0]
        result = [Interval(first.start, first.end)]
        for i in range(1, n):
            prev = result[-1]
            current = intervals[i]
            if prev.end >= current.start:
                prev.end = max(prev.end, current.end)
            else:
                result.append(Interval(current.start, current.end))
        return result