class TrieNode {
    private TrieNode[] child;
    private int freq;
    // Initialize your data structure here.
    public TrieNode() {
        child = new TrieNode[26];
        freq = 0;
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
}

public class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    public void insert(String word) {
        TrieNode node = root;
        
        for (int i = 0; i < word.length(); i++)
        {
            int index = word.charAt(i) - 'a';
            if (node.getIthChild(index) == null)
            {
                node.setIthChild(index);
                node = node.getIthChild(index);
            }
            else
                node = node.getIthChild(index);
        }
        node.increaseFreq(1);
    }

    // Returns if the word is in the trie.
    public boolean search(String word) {
        TrieNode node = root;
        for (int i = 0; i < word.length(); i++)
        {

            int index = word.charAt(i) - 'a';
            if (node.getIthChild(index) == null)
                return false;
            else
                node = node.getIthChild(index);
        }
        return node.getFreq() > 0;
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public boolean startsWith(String prefix) {
        TrieNode node = root;
        for (int i = 0; i < prefix.length(); i++)
        {
            int index = prefix.charAt(i) - 'a';
            if (node.getIthChild(index) == null)
                return false;
            else
                node = node.getIthChild(index);
        }
        return true;
    }
}

// Your Trie object will be instantiated and called as such:
// Trie trie = new Trie();
// trie.insert("somestring");
// trie.search("key");
