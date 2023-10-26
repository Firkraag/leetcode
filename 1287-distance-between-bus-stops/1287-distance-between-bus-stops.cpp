class Solution {
public:
  int distanceBetweenBusStops(vector<int> &distance, int start,
                              int destination) {
    int n = distance.size();
    int sum1 = 0;
    int sum2 = 0;
    for (int i = start; i != destination; i = (i + 1) % n) {
      sum1 += distance[i];
    }
    for (int i = start; i != destination;) {
		i = ((i - 1) % n + n) % n;
      sum2 += distance[i];
    }
    return min(sum1, sum2);
  }
};