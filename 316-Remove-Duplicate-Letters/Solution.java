public class Solution {
    public String removeDuplicateLetters(String s) {
        TreeMap<Character, ArrayList<Integer>> indices = new TreeMap<Character, ArrayList<Integer>>();
        for (int i = s.length() - 1; i >= 0; i--) {
            if (indices.containsKey(s.charAt(i))) {
                indices.get(s.charAt(i)).add(i);
            }
            else {
                ArrayList<Integer> list = new ArrayList<Integer>();
                list.add(i);
                indices.put(s.charAt(i), list);
            }
        }
        TreeSet<Integer> end = new TreeSet<Integer>();
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for(Map.Entry<Character, ArrayList<Integer>> entry : indices.entrySet()) {
            Character key = entry.getKey();
            ArrayList<Integer> value = entry.getValue();
            Integer index = value.get(0);
            map.put(key, index);
            end.add(index);
        }
        StringBuffer string = new StringBuffer();
        while (indices.size() != 0) {
            int minimum = end.first();
            for(Map.Entry<Character, ArrayList<Integer>> entry : indices.entrySet()) {
                Character key = entry.getKey();
                ArrayList<Integer> value = entry.getValue();
                int n = value.size();
                int index = value.get(n - 1);
                if (index <= minimum) {
                    string.append(key);
                    indices.remove(key);
                    end.remove(map.get(key));
                    for(Map.Entry<Character, ArrayList<Integer>> entry2 : indices.entrySet()) {
                        key = entry2.getKey();
                        value = entry2.getValue();
                        int i = value.size() - 1;
                        while (value.get(i) < index) {
                            value.remove(i);
                            i--;
                        }
                    }
                    break;
                }
            }
            
        }
    return string.toString();  
    }
    
}
