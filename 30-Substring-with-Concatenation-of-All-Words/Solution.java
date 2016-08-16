public class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        if (s.length() == 0 || words.length == 0 || words[0].length() == 0)
            return new ArrayList<Integer>();
        int n = s.length();
        int wordLength = words[0].length();
        int totalLength = words.length * words[0].length();
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
        //System.out.println("length of s: " + n + " length of words: " + words.length + "length of word: " + length);
        for (int k = 0; k < wordLength; k++) {
            if (k + totalLength > n) {
                break;
            }
            Map<String, Integer> number = new HashMap<String, Integer>(counter);
            int size = number.size();
            int i = k;
            int start = k;
            while (i < n) {
                String word = s.substring(i, Math.min(n, i + wordLength));
                if (number.containsKey(word)) {
                    int value = number.get(word);
                    if (value > 1) {
                        number.put(word, value - 1);
                    }
                    else if (value == 1) {
                        number.put(word, value - 1);
                        size--;
                        if (size == 0) {
                            result.add(start);
                            number.put(s.substring(start, start + wordLength), 1);
                            start += wordLength;
                            size = 1;
                        }
                    }
                    else {
                        int j = start;
                        while (!word.equals(s.substring(j, j + wordLength))) {
                            String startWord = s.substring(j, j + wordLength);
                            value = number.get(startWord);
                            if (value == 0) {
                                size++;
                            }
                            number.put(startWord, value + 1);
                            j += wordLength;
                        }
                        start = j + wordLength;
                    }
                    i += wordLength;
                }
                else {
                    i += wordLength;
                    if (n - i < totalLength) {
                        break;
                    }
                    else {
                        start = i;
                        number = new HashMap<String, Integer>(counter);
                        size = number.size();
                    }
                }
            }
        }
//        System.out.println("number of loops: " + c);
        return result;
    }
}
