#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        #left[i] is the max profit of array prices[1:i]
        left = self.computeLeft(prices)
        #right[i] is the max profit of array prices[i:n] 
        right = self.computeRight(prices)
        return max(left[-1], max([left[i] + right[i + 1] for i in range(n - 1)]))
    
    def computeLeft(self, prices):
        n = len(prices)
        one = [0] * n
        minimum = prices[0]
        for i in range(1, n):
            if minimum < prices[i]:
                one[i] = max(one[i - 1], prices[i] - minimum)
            else:
                minimum = prices[i]
                one[i] = one[i - 1]
        return one
        
    def computeRight(self, prices):
        n = len(prices)
        one = [0] * n
        maximum = prices[-1]
        for i in range(n - 2, -1, -1):
            if maximum > prices[i]:
                one[i] = max(one[i + 1], maximum - prices[i])
            else:
                maximum = prices[i]
                one[i] = one[i + 1]
        return one
