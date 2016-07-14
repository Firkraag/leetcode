public class Solution {
    public boolean isValid(String s) {
        int n = s.length();
        Stack<Character> stack = new Stack<Character>();
        HashMap<Character, Character> d = new HashMap<Character, Character>();
        HashSet<Character> se = new HashSet<Character>();
        d.put('[', ']');
        d.put('{', '}');
        d.put('(', ')');
        se.add(']');
        se.add(')');
        se.add('}');
        
        for (int i = n - 1; i >= 0; i--) {
            if (d.containsKey(s.charAt(i))) {
                if (stack.size() == 0)
                    return false;
                else {
                    char c = stack.pop();
                    if (c != d.get(s.charAt(i)))
                        return false;
                }
            }
            else {
                stack.push(s.charAt(i));
            }
        }
        if (stack.size() == 0)
            return true;
        else
            return false;
    }
}
