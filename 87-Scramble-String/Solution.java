public class Solution {
    public boolean isScramble(String s1, String s2) {
        int n = s1.length();
        if (n == 0)
            return true;
        else {
            boolean[][][] scramble = new boolean[n][n][n];
            for (int i1 = 0; i1 < n; i1++)
                for (int i2 = 0; i2 < n; i2++)
                    scramble[0][i1][i2] = s1.charAt(i1) == s2.charAt(i2);
            for (int l = 2; l < n + 1; l++) {
                for (int i1 = 0; i1 < n - l + 1; i1++) {
                    for (int i2 = 0; i2 < n - l + 1; i2++) {
                        int j1 = i1 + l - 1;
                        int j2 = i2 + l - 1;
                        boolean status = false;
                        for (int k = 1; k < l; k++) {
                            status = (scramble[k - 1][i1][i2] && scramble[l - k - 1][i1 + k][i2 + k]) || (scramble[k - 1][i1][i2 + l - k] && scramble[l - k - 1][i1 + k][i2]);
                            if (status)
                                break;
                        }
                        scramble[l - 1][i1][i2] = status;
                    }
                }
            }
            return scramble[n - 1][0][0];
        }
    }
}
