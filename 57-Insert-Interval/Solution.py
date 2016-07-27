# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        n = len(intervals)
        if n == 0:
            return [newInterval]
        start = newInterval.start
        new = []
        i = 0
        while i < n:
            if start <= intervals[i].start:
                new.append(newInterval)
                break
            else:
                new.append(intervals[i])
                i += 1
        if i == n:
            new.append(newInterval)
        else:
            new.extend(intervals[i:])
        intervals = new
        #print [[interval.start, interval.end] for interval in new]
        first = intervals[0]
        result = [Interval(first.start, first.end)]
        for i in range(1, n + 1):
            prev = result[-1]
            current = intervals[i]
            if prev.end >= current.start:
                prev.end = max(prev.end, current.end)
            else:
                result.append(Interval(current.start, current.end))
        return result
