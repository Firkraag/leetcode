class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> scores;
        int sum = 0;
        for (const auto &operation:operations) {
            if (operation == "+") {
                scores.push_back(scores.back() + scores[scores.size() - 2]);
                sum += scores.back();
            }
            else if (operation == "D") {
                scores.push_back(2 * scores.back());
                sum += scores.back();
            }
            else if (operation == "C") {
                sum -= scores.back();
                scores.pop_back();
            }
            else {
                scores.push_back(stoi(operation));
                sum += scores.back();
            }
            
        }
        return sum;
    }
};