class Solution {
public:
    int maxCoins(vector<int>& piles) {
        sort(piles.begin(), piles.end(), greater<int>());
        int n = piles.size();
        int sum = 0;
        for (int i = 0; i < n / 3; i++) {
            sum += piles[2 * i + 1];
        }
        return sum;
    }
};