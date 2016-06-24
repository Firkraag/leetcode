#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        one = [0] * n
        minimum = prices[0]
        for i in range(1, n):
            if minimum < prices[i]:
                one[i] = max(one[i - 1], prices[i] - minimum)
            else:
                minimum = prices[i]
                one[i] = one[i - 1]
            #print minimum, one
        return one[-1]
