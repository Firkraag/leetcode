class Solution {
    constexpr static int tables[20] = {1,2,5,14,42,132,429,1430,4862,16796,58786,208012,742900,2674440,9694845,35357670,129644790,477638700,1767263190};
public:
    int numTrees(int n) {
      int nums[20] = {1, 1,2,5,14,42};
      for (int i = 6; i <= n; i++) {
          int result = 0;
          for (int j = 1; j <= i; j++) {
              result += nums[j - 1] * nums[i - j]; 
          }
          nums[i] = result;
      }
      return nums[n];
    }
};