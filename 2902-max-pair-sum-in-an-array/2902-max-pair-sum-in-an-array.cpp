using namespace std;
class Solution {
    int maxDigit(int num) {
        int maxDigit = 0;
        while (num) {
            maxDigit = max(maxDigit, num % 10);
            num /= 10;
        }
        return maxDigit;
    }
public:
    int maxSum(vector<int>& nums) {
        unordered_map<int, vector<int> > groupByMaxDigit;
        for (const auto &num: nums) {
            int digit = maxDigit(num);
            groupByMaxDigit[digit].push_back(num);
        }
        int ans = -1;
        for (auto &it : groupByMaxDigit) {
            auto &list = it.second;
            if (list.size() >= 2) {
                sort(list.begin(), list.end(), greater<int>());
                ans = max(ans, list[0] + list[1]);
            }
        }
        return ans;
    }
};