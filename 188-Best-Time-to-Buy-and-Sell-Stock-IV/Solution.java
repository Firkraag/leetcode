public class Solution {
    public int maxProfit(int k, int[] prices) {
        int n = prices.length;
        if (n <= 1 || k <= 0) {
            return 0;
        }
        else if (k >= n / 2) {
            int profit = 0;
            int minimum = prices[0];
            for (int i = 1; i < n; i++) {
                if (prices[i] > minimum) {
                    profit += prices[i] - minimum;
                }
                minimum = prices[i];
            }
            return profit;
        }
        else {
            int[] dp = new int[n + 1];
            dp[0] = 0;
            dp[1] = 0;
            for (int l = 1; l < k + 1; l++) {
                int m2 = -prices[0];
                for (int i = 2; i < n + 1; i++) {
                    int profit = Math.max(dp[i - 1], m2 + prices[i - 1]);
                    m2 = Math.max(m2, dp[i] - prices[i - 1]);
                    dp[i] = profit;
                }
            }
            return dp[n];
        }
    }
}
