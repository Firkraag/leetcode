class Solution {
public:
    int oddCells(int m, int n, vector<vector<int>>& indices) {
        int matrix[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = 0;
            }
        }
        for (const auto &index : indices) {
            int rowIndex = index[0];
            int colIndex = index[1];
            for (int i = 0; i < n; i++) {
                matrix[rowIndex][i]++;
            }
            for (int i = 0; i < m; i++) {
                matrix[i][colIndex]++;
            }
        }
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                count += matrix[i][j] % 2;
            }
        }
        return count;
    }
};