#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        return self.trapAux(height, 0, len(height) - 1)
        
    def trapAux(self, height, start, end):
        if end - start + 1 <= 2:
            return 0
        if height[start] >= height[start + 1]:
            maximum = start
            second = start + 1
        else:
            maximum = start + 1
            second = start
        for i in range(start + 2, end + 1):
            if height[i] > height[maximum]:
                second = maximum
                maximum = i
            elif height[i] > height[second]:
                second = i
            #print "wowow", maximum, second
        low = min(second, maximum)
        high = max(second, maximum)
        # low, high
        #print (high - low - 1) * height[second] - sum(height[low + 1:high])
        #print height[low], height[high]
        return (high - low - 1) * height[second] - sum(height[low + 1:high]) + self.trapAux(height, start, low) + self.trapAux(height, high, end)
