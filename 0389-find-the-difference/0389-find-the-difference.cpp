class Solution {
public:
    char findTheDifference(string s, string t) {
        auto func = bit_xor<char>();
        return accumulate(s.begin(), s.end(), 0, func) ^ accumulate(t.begin(), t.end(), 0, func);
    }
};