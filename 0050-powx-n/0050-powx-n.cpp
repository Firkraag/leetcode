class Solution {
    double myPowAux(double x, int n) {
        double result = x;
        vector<double> multiple;
        for (int val = n; val > 1; val /= 2) {
            if (val % 2) {
                multiple.push_back(x);
            }
            else {
                multiple.push_back(1);
            }
        }
        while (!multiple.empty()) {
            result = result * result * multiple.back();
            multiple.pop_back();
        }
        return result;
    }
public:
    double myPow(double x, int n) {
        if (x == 0) {
            return 0;
        }
        if (n == 0) {
            return 1;
        }
        if (x == 1) {
            return 1;
        }
        if (x == -1) {
            return n % 2 ? -1 : 1;
        }
        if (n == INT_MIN) {
            return 1/(myPowAux(x, INT_MAX) * x);
        }
        double result = myPowAux(x, abs(n));
        return n < 0 ? 1 / result : result;
    }
};