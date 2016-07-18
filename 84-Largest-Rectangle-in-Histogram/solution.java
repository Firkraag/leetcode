public class Solution {
    public int largestRectangleArea(int[] heights) {
        return largestRectangleAreaAux(heights, 0, heights.length - 1);
    }
    private int largestRectangleAreaAux(int[] heights, int p, int r) {
        if (p > r)
            return 0;
        else if (p == r)
            return heights[p];
        else {
            int mid = (p + r) / 2;
            int area1 = largestRectangleAreaAux(heights, p, mid);
            int area2 = largestRectangleAreaAux(heights, mid + 1, r);
            int minHeight = Math.min(heights[mid], heights[mid + 1]);
            int area = 2 * minHeight;
            int i = mid - 1;
            int j = mid + 2;
            while (i >= p && j <= r) {
                if (heights[i] >= heights[j]) {
                    minHeight = Math.min(heights[i], minHeight);
                    area = Math.max(area, minHeight * (j - i));
                    i--;
                }
                else {
                    minHeight = Math.min(heights[j], minHeight);
                    area = Math.max(area, minHeight * (j - i));
                    j++;
                }
            }
            if (i >= p) 
                while (i >= p) {
                    minHeight = Math.min(heights[i], minHeight);
                    area = Math.max(area, minHeight * (r - i + 1));
                    i--;
                }
            else {
                while (j <= r) {
                    minHeight = Math.min(heights[j], minHeight);
                    area = Math.max(area, minHeight * (j - p + 1));
                    j++;
                }
            }
            return Math.max(area1, Math.max(area2, area));
        }
    }
}
