public class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        int ans = Integer.MIN_VALUE, row = matrix.length, col = matrix[0].length;
        for (int left = 0; left < col; left++) {
            int[] helper = new int[row];
            for (int right = left; right < col; right++) {
                for (int i = 0; i < helper.length; i++) {
                    helper[i] += matrix[i][right];
                }
                int sumRight = 0;
                TreeSet<Integer> ts = new TreeSet<>();
                ts.add(0);  // this is important. without this, won't pass {1, 0}
                for (int i : helper) {
                    sumRight += i;
                    Integer sumLeft = ts.ceiling(sumRight - k);
                    if (sumLeft != null) {
                        ans = Math.max(ans, sumRight - sumLeft);
                    }
                    ts.add(sumRight);
                }   // for
            }   // for
        }
        return ans;
    }
    
}
