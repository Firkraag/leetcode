class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = INT_MIN;
        int endPointMaxSum = 0;
        for (const int num:nums) {
            if (endPointMaxSum < 0) {
                endPointMaxSum = num;
            }
            else {
                endPointMaxSum += num;
            }
            maxSum = max(endPointMaxSum, maxSum);
        }
        return maxSum;
    }
};