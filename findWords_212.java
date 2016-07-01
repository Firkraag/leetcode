class TrieNode {
    private TrieNode[] child;
    private int freq;
    private boolean searched;
    
    // Initialize your data structure here.
    public TrieNode() {
        child = new TrieNode[26];
        freq = 0;
        searched = false;
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
    public boolean getSearched() {
        return searched;
    }
    public void setSearched(boolean searched) {
        this.searched = searched;
    }
}

class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public TrieNode getRoot()
    {
        return root;
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

public class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        int m = board.length;
        int n = board[0].length;
        Trie trie = new Trie();
        ArrayList<String> solutions = new ArrayList<String>();
        StringBuffer partial = new StringBuffer();
        boolean[][] status = new boolean[m][n];
        
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                status[i][j] = false;
                
        for (String word : words)
            trie.insert(word);
            
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                search(board, i, j, trie.getRoot(), solutions, status, partial);
        return solutions;
    }
    
    private void search(char[][] board, int i, int j, TrieNode node, ArrayList<String> solutions, boolean[][] status, StringBuffer partial) {
        int m = board.length;
        int n = board[0].length;

        if (status[i][j])
            return;
        int index = board[i][j] - 'a';
        if (node.getIthChild(index) == null)
            return;
        else
        {
            node = node.getIthChild(index);
            partial.append(board[i][j]);
            status[i][j] = true;
            if (node.getFreq() > 0 && node.getSearched() == false)
            {
                solutions.add(partial.toString());
                node.setSearched(true);
            }
            if (i > 0)
                search(board, i - 1, j, node, solutions, status, partial);
            if (i < m - 1)
                search(board, i + 1, j, node, solutions, status, partial);
            if (j > 0)
                search(board, i, j - 1, node, solutions, status, partial);
            if (j < n - 1)
                search(board, i, j + 1, node, solutions, status, partial);
            status[i][j] = false;
            partial.deleteCharAt(partial.length() - 1);
        }
    }
}
