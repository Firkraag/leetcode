class Solution {
public:
  int distanceBetweenBusStops(vector<int> &distance, int start, int destination) {
    if (start > destination) swap(start, destination);

    int sum1 = 0; // Clockwise distance
    int totalDistance = 0;

    for (int i = 0; i < distance.size(); ++i) {
      if (i >= start && i < destination) {
        sum1 += distance[i];
      }
      totalDistance += distance[i];
    }

    int sum2 = totalDistance - sum1; // Counter-clockwise distance

    return min(sum1, sum2);
  }
};
