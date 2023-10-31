class Solution {
public:
    int longestContinuousSubstring(string s) {
        int n = s.size();
        int maxLength = 1;
        int start = 0;
        for (int i = 1; i < n; i++) {
            if (s[i] != s[i - 1] + 1) {
                maxLength = max(maxLength, i - start);
                start = i;
            }
        }
        return max(maxLength, n - start);
    }
};