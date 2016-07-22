class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        else:
            profit = 0
            minimum = prices[0]
            for i in range(1, n):
                if prices[i] > minimum:
                    profit += prices[i] - minimum
                minimum = prices[i]
            return profit
            