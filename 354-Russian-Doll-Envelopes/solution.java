public class Solution {
    public int maxEnvelopes(int[][] envelopes) {
        int n = envelopes.length;
        if (n == 0)
            return 0;
        else if (n == 1)
            return 1;
        Arrays.sort(envelopes, new PairComparator());
        int[] nest = new int[n];
        for (int i = 0; i < n; i++)
            nest[i] = 1;
        ArrayList<int[]> ranges = computeRanges(envelopes);
        n = ranges.size();
        for (int i = n - 1; i >= 0; i--) {
            for (int k = ranges.get(i)[0]; k <= ranges.get(i)[1]; k++) {
                int[] envelope = envelopes[k];
                for (int j = i + 1; j < n; j++) {
                    int left = ranges.get(j)[0];
                    int right = ranges.get(j)[1];
                    int index = binarySearch(envelopes, left, right + 1, envelope[1]);
                    if (index != right + 1)
                        nest[k] = Math.max(nest[index] + 1, nest[k]);
                }
            }
        }
        int maximum = Integer.MIN_VALUE;
        for (int value: nest) {
            if (value > maximum)
                maximum = value;
        }
        return maximum;
    }
    private ArrayList<int[]> computeRanges(int[][] envelopes) {
        ArrayList<int[]> ranges = new ArrayList<int[]>();
        int n = envelopes.length;
        int i = 0;
        while (i < n) {
            int left = i;
            while (i < n - 1 && envelopes[i][0] == envelopes[i + 1][0])
                i++;
            int right = i;
            int[] pair = new int[2];
            pair[0] = left;
            pair[1] = right;
            ranges.add(pair);
            i++;
        }
        return ranges;
    }
   
    private int binarySearch(int[][] envelopes, int left, int right, int target) {
        while (left < right) {
            int mid = (left + right) / 2;
            if (target < envelopes[mid][1])
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }
}

class PairComparator implements Comparator<int[]> {
    public int compare(int[] a, int[] b) {
        if (a[0] < b[0])
            return -1;
        else if (a[0] > b[0])
            return 1;
        else {
            if (a[1] < b[1])
                return -1;
            else if (a[1] > b[1])
                return 1;
            else
                return 0;
        }
    }
}
    
