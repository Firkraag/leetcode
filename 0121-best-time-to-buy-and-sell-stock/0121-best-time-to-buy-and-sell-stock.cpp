class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        for (int i = 1, prefixMin = prices[0], prefixMax = prices[0]; i < prices.size(); i++) {
          int price = prices[i];
          if (price <= prefixMin) {
            prefixMin = price;
          } else  {
            maxProfit = max(maxProfit,  price - prefixMin);
            prefixMax = price > prefixMax ? price : prefixMax;
          } 
        }
        return maxProfit;
    }
};