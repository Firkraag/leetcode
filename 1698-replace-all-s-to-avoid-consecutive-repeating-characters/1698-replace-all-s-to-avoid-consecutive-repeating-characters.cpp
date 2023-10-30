#include <string>
#include <algorithm>

class Solution {
public:
    std::string modifyString(std::string s) {
        int n = s.size();

        for (int i = 0; i < n; i++) {
            if (s[i] == '?') {
                char prev = (i == 0) ? '?' : s[i - 1];
                char next = (i == n - 1) ? '?' : s[i + 1];

                char replacement = 'a';
                while (replacement == prev || replacement == next) {
                    replacement++;
                }

                s[i] = replacement;
            }
        }

        return s;
    }
};
