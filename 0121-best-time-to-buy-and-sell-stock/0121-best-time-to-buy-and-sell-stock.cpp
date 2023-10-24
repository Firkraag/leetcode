class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int maxProfit = 0;
        int prefixMin = prices[0];
        int prefixMax = prices[0];
        for (int i = 1; i < n; i++) {
          int price = prices[i];
          if (price <= prefixMin) {
            prefixMin = price;
          } else if (price < prefixMax) {
            maxProfit = max(maxProfit,  price - prefixMin);
          } else {
            prefixMax = price;
            maxProfit = prefixMax - prefixMin;
          }
        }
        return maxProfit;
    }
};