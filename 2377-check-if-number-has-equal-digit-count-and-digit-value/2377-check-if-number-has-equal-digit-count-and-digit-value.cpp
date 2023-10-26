class Solution {
public:
    bool digitCount(string num) {
        int n = num.size();
        int count[10] = {0};
        for (const char c: num) {
            if (c - '0' < n) {
                count[c - '0']++;
            }
        }
        for (int i = 0; i < n; i++) {
            if (count[i] != num[i] - '0') {
                return false;
            }
        }
        return true;
    }
};