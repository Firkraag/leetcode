public class Solution {
    public List<List<Integer>> palindromePairs(String[] words) {
        int n = words.length;
        boolean[][] v = new boolean[n][n];
        HashMap<String, Integer> h = new HashMap();
        List<List<Integer>> ans = new ArrayList();
        for (int i = 0; i < words.length; h.put(words[i], i), v[i][i] = true, i++);
        
        for (int i = 0; i < n; i++) {
            List<String> palinMatch = findPalinMatch(words[i]);
            for (String cand : palinMatch)
                if (h.containsKey(cand) && !v[h.get(cand)][i]) {
                    ans.add(Arrays.asList(h.get(cand), i));
                    v[h.get(cand)][i] = true;
                }
                    
            palinMatch = findPalinMatch(new StringBuilder(words[i]).reverse().toString());
            for (String cand : palinMatch) {
                String candR = new StringBuilder(cand).reverse().toString();
                if (h.containsKey(candR) && !v[i][h.get(candR)]) {
                    ans.add(Arrays.asList(i, h.get(candR)));
                    v[i][h.get(candR)] = true;
                }
            }
        }
        
        return ans;
    }
    
    private List<String> findPalinMatch(String s) {
        String y = s + "#" + new StringBuilder(s).reverse().toString();
        int len = y.length();
        int[] p = new int[len]; // find KMP table
        p[0] = 0;
        for (int i = 1; i < len; i++) {
            int j = p[i - 1];
            while (j > 0 && y.charAt(i) != y.charAt(j)) j = p[j - 1];
            p[i] = (y.charAt(i) != y.charAt(j)) ? 0 : j + 1;
        }
        
        List<String> res = new ArrayList();
        for (int j = p[len - 1]; j > 0; j = p[j - 1])
            res.add(y.substring(len - s.length(), len - j));
        res.add(y.substring(len - s.length()));
        return res;    
    }
}