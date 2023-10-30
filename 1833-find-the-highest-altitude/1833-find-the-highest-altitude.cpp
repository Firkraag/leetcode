class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int maximum = 0;
        int prev = 0;
        for (const int delta: gain) {
            prev += delta;
            maximum = max(maximum, prev);
        }
        return maximum;
    }
};