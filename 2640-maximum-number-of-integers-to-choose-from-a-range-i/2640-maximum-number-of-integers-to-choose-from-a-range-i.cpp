class Solution {
public:
    int maxCount(vector<int>& banned, int n, int maxSum) {
        unordered_set<int> bannedSet{banned.begin(), banned.end()};
        int numInts = 0;
        for (int i = 1, sum = 0; i <= n && i + sum <= maxSum; i++) {
            if (bannedSet.contains(i)) {
                continue;
            }
            else {
                sum += i;
                numInts++;
            }
        }
        return numInts;
    }
};