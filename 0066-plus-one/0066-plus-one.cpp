class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int promote = 1;
        int n = digits.size();
        vector<int> ans(n + 1);
        for (int i = n - 1; i >= 0; i--) {
            ans[i + 1] = (digits[i] + promote) % 10;
            promote = (digits[i] + promote) / 10;
        }
        if (promote == 1) {
            ans[0] = 1;
            return ans;
        }
        else {
            return {ans.begin() + 1, ans.end()};
        }
    }
};