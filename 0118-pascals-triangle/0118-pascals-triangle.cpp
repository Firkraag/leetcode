class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> values = {{1},{1,1},{1,2,1},{1,3,3,1},{1,4,6,4,1}};
        for (int i = values.size(); i < numRows; i++) {
            vector<int> row;
            row.reserve(i + 1);
            auto &prevRow = values[i - 1];
            row.push_back(1);
            for (int j = 0; j < i - 1; j++) {
                row.push_back(prevRow[j] + prevRow[j + 1]);
            }
            row.push_back(1);
            values.push_back(row);
        }
        return {values.begin(), values.begin() + numRows};
    }
};