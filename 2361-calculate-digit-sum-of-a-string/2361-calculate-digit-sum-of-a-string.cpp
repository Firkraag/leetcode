class Solution {
public:
    string digitSum(string s, int k) {
        int length = s.size();
        while (length > k) {
            int pos = 0;
            for (int i = 0; i < length; i += k) {
                int sum = 0;
                for (int j = i; j < min(length, i + k); j++) {
                    sum += s[j] - '0';
                }
                for (char c: to_string(sum)) {
                    s[pos++] = c;
                }
            }
            cout << s << " " << pos << endl;
            length = pos;
        }
        return {s.begin(), s.begin() + length};
    }
};