class Solution {
public:
    bool isThree(int n) {
        if (n < 4) {
            return false;
        }
        int x = (int) sqrt(n);
        for (int i = 2; i < x; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return x * x == n;        
    }
};