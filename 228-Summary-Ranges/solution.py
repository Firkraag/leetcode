class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i = 0
        summary = []
        n = len(nums)
        while i <= n - 1:
            start_index = i
            while i < n - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            if start_index == i:
                summary.append(str(nums[i]))
            else:
                summary.append("%s->%s" % (str(nums[start_index]), str(nums[i])))
            i += 1
        return summary
