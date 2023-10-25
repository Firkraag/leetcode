class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), [](const auto &point1, const auto &point2) {return point1[0] < point2[0];});
        int widest = 0;
        for (int i = 1; i < points.size(); i++) {
          widest = max(widest, points[i][0] - points[i - 1][0]);
        }
        return widest;
    }
};