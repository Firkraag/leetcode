public class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        int maximum = 0;
        for (int i = 0; i < n; i++) {
            int borderHeight = Integer.MAX_VALUE;
            int borderMax = Integer.MIN_VALUE;
            for (int j = i; j >= 0; j--) {
                borderHeight = Math.min(borderHeight, heights[j]);
                borderMax = Math.max(borderHeight * (i - j + 1), borderMax);
            }
            maximum = Math.max(borderMax, maximum);
        }
        return maximum;
    }
}