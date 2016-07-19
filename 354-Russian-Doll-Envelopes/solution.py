class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        envelopes = sorted(envelopes)
        nests = []
        ranges = self.computeRanges(envelopes)
        n = len(ranges)
        for i in range(n):
            rangeHeight = []
            rangeNest = []
            for index in range(ranges[i][0], ranges[i][1] + 1):
                height = envelopes[index][1]
                rangeHeight.append(height)
                rangeNest.append(1)
                low = 0
                high = len(nests) - 1
                while low <= high:
                    mid = (low + high) / 2
                    if nests[mid] < height:
                        rangeNest[-1] = mid + 2
                        low = mid + 1
                    else:
                        high = mid - 1
            for j in range(len(rangeHeight)):
                nest = rangeNest[j]
                height = rangeHeight[j]
                if nest > len(nests):
                    nests.append(height)
                elif height < nests[nest - 1]:
                    nests[nest - 1] = height
        return len(nests)
    def computeRanges(self, envelopes):
        ranges = []
        n = len(envelopes)
        i = 0
        while i < n:
            left = i
            while i < n - 1 and envelopes[i][0] == envelopes[i + 1][0]:
                i += 1
            right = i
            ranges.append((left, right))
            i += 1
        return ranges
    
