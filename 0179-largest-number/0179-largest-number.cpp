class Solution {
public:
    string largestNumber(vector<int>& nums) {
        if (all_of(nums.begin(), nums.end(), [](const auto &num) {return num == 0;})) {return "0";}
        vector<string> strings;
        strings.reserve(nums.size());
        for (const auto &num: nums) {
            strings.push_back(to_string(num));
        }
        sort(strings.begin(), strings.end(), [](const string &str1,const string &str2) {return str1 + str2 > str2 + str1;});
        string ans;
        for (const auto &str: strings) {
            ans.append(str);
        }
        return ans;
    }
};