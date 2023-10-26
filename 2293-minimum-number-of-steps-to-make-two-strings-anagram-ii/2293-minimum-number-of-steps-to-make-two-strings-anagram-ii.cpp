class Solution {
public:
    int minSteps(string s, string t) {
        int counter[26];
        for (int i = 0; i < 26; i++) {
            counter[i] = 0;
        }
        for (const char c: s) {
            counter[c - 'a']++;
        }
        for (const char c: t) {
            counter[c - 'a']--;
        }
        int steps = 0;
        for (int i = 0; i < 26; i++) {
            steps += abs(counter[i]);
        }
        return steps;
    }
};