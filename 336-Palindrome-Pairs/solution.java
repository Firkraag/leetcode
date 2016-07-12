class TrieNode {
    private TrieNode[] child;
    private int freq;
    private int index;
    private HashSet<Integer> set;
    // Initialize your data structure here.
    public TrieNode() {
        child = new TrieNode[26];
        freq = 0;
        index = -1;
        set = new HashSet<Integer>();
    }

    public TrieNode getIthChild(int i) {
        return child[i];
    }
    public void setIthChild(int i)
    {
        child[i] = new TrieNode();
    }
    public int getFreq()
    {
        return freq;
    }
    public void increaseFreq(int delta)
    {
        freq += delta;
    }
    public int getIndex() {
        return index;
    }
    public void setIndex(int index) {
        this.index = index;
    }
    public HashSet<Integer> getSet() {
        return set;
    }
}

class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public TrieNode getRoot() {
        return root;
    }
    // Inserts a word into the trie.
    public void insert(StringBuffer word, int idx) {
        TrieNode node = root;
        
        for (int i = 0; i < word.length(); i++)
        {
            int index = word.charAt(i) - 'a';
            node.getSet().add(new Integer(idx));
            if (node.getIthChild(index) == null)
            {
                node.setIthChild(index);
                node = node.getIthChild(index);
            }
            else
                node = node.getIthChild(index);
        }
        node.increaseFreq(1);
        node.setIndex(idx);
    }

}

public class Solution {
    public List<List<Integer>> palindromePairs(String[] words) {
        Trie trie = new Trie();
        int n = words.length;
        ArrayList<List<Integer>> pairs = new ArrayList<List<Integer>>();
        ArrayList<ArrayList<Integer>> RLs = new ArrayList<ArrayList<Integer>>();
        
        for (int i = 0; i < n; i++)
        {
            trie.insert((new StringBuffer(words[i])).reverse(), i);
            RLs.add(manacher(words[i]));
        }
        for (int i = 0; i < n; i++)
            findPair(words, trie, pairs, i, RLs);
        return pairs;
    }
    
    private void findPair(String[] words, Trie trie, ArrayList<List<Integer>> pairs, int wordIndex, ArrayList<ArrayList<Integer>> RLs)
    {
        String word = words[wordIndex];
        TrieNode node = trie.getRoot();
        int n = word.length();
        int i = 0;
        
        while (i < n)
        {
            char c = word.charAt(i);
            int index = c - 'a';
            if (node.getFreq() > 0)
            {
                if (wordIndex != node.getIndex() && isPalindrome(word, i, n - 1, RLs.get(wordIndex)))
                {
                    List<Integer> pair = new ArrayList<Integer>();
                    pair.add(new Integer(wordIndex));
                    pair.add(new Integer(node.getIndex()));
                    pairs.add(pair);
                }
            }
            if (node.getIthChild(index) == null)
                return;
            else
            {
                node = node.getIthChild(index);
                i++;
            }
        }
        postProcessing(node, pairs, words, wordIndex, RLs);
        
    }
    
    private void postProcessing(TrieNode node, ArrayList<List<Integer>> pairs, String[] words, int wordIndex, ArrayList<ArrayList<Integer>> RLs)
    {
        if (node.getFreq() > 0 && wordIndex != node.getIndex())
        {
            List<Integer> pair = new ArrayList<Integer>();
            pair.add(new Integer(wordIndex));
            pair.add(new Integer(node.getIndex()));
            pairs.add(pair);
        }
        int n = words[wordIndex].length();
        for (int index: node.getSet())
        {
            String word = words[index];
            if (isPalindrome(word, 0, word.length() - n - 1, RLs.get(index)))
            {
                List<Integer> pair = new ArrayList<Integer>();
                pair.add(new Integer(wordIndex));
                pair.add(new Integer(index));
                pairs.add(pair);
            }
        }
    }
    
    private ArrayList<Integer> manacher(String s)
    {
        StringBuilder str = new StringBuilder();
        str.append('#');
        for (int i = 0; i < s.length(); i++)
        {
            str.append(s.charAt(i));
            str.append('#');
        }
        int MaxRight = 0;
        int pos = 0;
        int MaxLen = 0;
        int[] rl = new int[str.length()];

        for (int i = 0; i < str.length(); i++)
        {
            if (i < MaxRight)
                rl[i] = Math.min(rl[2 * pos - i], MaxRight - i);
            else
                rl[i] = 1;
            while (i -  rl[i] >= 0 && i + rl[i] < str.length() && str.charAt(i - rl[i]) == str.charAt(i + rl[i]))
                rl[i] += 1;
            if (rl[i] + i - 1 > MaxRight)
            {
                MaxRight = rl[i] + i - 1;
                pos = i;
            }
            MaxLen = Math.max(MaxLen, rl[i]);
        }
        ArrayList<Integer> RL = new ArrayList<Integer>();
        for (int i: rl)
        {
            RL.add(new Integer(i));
        }
        return RL;
    }
    
    private boolean isPalindrome(String s, int start, int end, ArrayList<Integer> RL) {
        int pos = start + end + 1;
        return start >= (pos - RL.get(pos).intValue() + 1) / 2 && (pos + RL.get(pos).intValue() - 1) / 2 >= end;
    }
    
}
