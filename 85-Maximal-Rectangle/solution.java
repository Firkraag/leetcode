public class Solution {
    public int maximalRectangle(char[][] matrix) {
        int m = matrix.length;
        if (m == 0)
            return 0;
        int n = matrix[0].length;
        if (n == 0)
            return 0;
        int maxArea = 0;
        boolean[][] bool = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                bool[i][j] = true;
            }
        }
        for (int l = 1; l <= m; l++) {
            for (int i = 0; i < m - l + 1; i++) {
                int j = i + l - 1;
                int maxLength = 0;
                int length = 0;
                for (int k = 0; k < n; k++) {
                    bool[i][k] = bool[i][k] && (matrix[j][k] == '1');
                    if (bool[i][k])
                        length++;
                    else {
                        maxLength = Math.max(maxLength, length);
                        length = 0;
                    }
                }
                maxLength = Math.max(maxLength, length);
                maxArea = Math.max(maxArea, maxLength * l);
            }
        }
        return maxArea;
    }
}
