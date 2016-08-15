public class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        int n = s.length();
        if (words.length == 0)
            return new ArrayList<Integer>();
        int length = words[0].length();
        List<Integer> result = new ArrayList<Integer>();
        Map<String, Integer> counter = new HashMap<String, Integer>();
        for (String word: words) {
            if (counter.containsKey(word)) {
                counter.put(word, counter.get(word) + 1);
            }
            else {
                counter.put(word, 1);
            }
        }
        System.out.println("length of s: " + n + " length of words: " + words.length + "length of word: " + length);
        int c = 0;
        for (int i = 0; i < n - length * words.length + 1; i++) {
            Map<String, Integer> number = new HashMap<String, Integer>(counter);
            int start = i;
            int j = i;
            while (number.size() > 0 && j + length <= n && number.containsKey(s.substring(j, j + length))) {
                c++;
                String word = s.substring(j, j + length);
                number.put(word, number.get(word) - 1);
                if (number.get(word) == 0)
                    number.remove(word);
                j += length;
            }
            if (number.isEmpty()) {
                result.add(start);
            }
            
        }
        System.out.println("number of loops: " + c);
        return result;
    }
}

