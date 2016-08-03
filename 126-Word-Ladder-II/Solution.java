public class Solution {
    public List<List<String>> findLadders(String beginWord, String endWord, Set<String> wordList) {
    	if (beginWord == endWord) {
    		ArrayList<List<String>> solution = new ArrayList<List<String>>();
    		for (String word: wordList) {
    			if (isAdjacent(beginWord, word)) {
    				List<String> path = new ArrayList<String>();
    				path.add(beginWord);
    				path.add(word);
    				path.add(endWord);
    				solution.add(path);
    			}
    		}
    		return solution;
    	}
    	else {
			Vertex source = new Vertex(beginWord);
	        Vertex sink = new Vertex(endWord);
	        wordList.remove(beginWord);
	        wordList.remove(endWord);
	        Graph graph = constructGraph(beginWord, endWord, wordList, source, sink);
	        return graph.findAllPaths(source, sink);
    	}
	        
    }

    private Graph constructGraph(String beginWord, String endWord, Set<String> wordList, Vertex source, Vertex sink) {
    	int n = wordList.size();
    	HashMap<Vertex, ArrayList<Vertex>> adj = new HashMap<Vertex, ArrayList<Vertex>>();
        Vertex[] vertices = new Vertex[n + 2];
        HashMap<String, Vertex> mapping = new HashMap<String, Vertex>();
        int j = 0;
        for (String word : wordList) {
            Vertex vertex = new Vertex(word);
            vertices[j++] = vertex;
            adj.put(vertex, new ArrayList<Vertex>());
            mapping.put(word, vertex);
        }
        vertices[n] = source;
        vertices[n + 1] = sink;
        adj.put(source, new ArrayList<Vertex>());
        adj.put(sink, new ArrayList<Vertex>());
        mapping.put(beginWord, source);
        mapping.put(endWord, sink);
    	Set<String> set = new HashSet<String>();
        wordList.add(endWord);
        set.add(beginWord);
        while (!set.isEmpty() && !set.contains(endWord)) {
            Set<String> temp = new HashSet<String>();
            for (String word : set) {
                char[] chs = word.toCharArray();
                Vertex u = mapping.get(word);
                for (int i = 0; i < chs.length; i++) {
                    for (char c = 'a'; c <= 'z'; c++) {
                        char old = chs[i];
                        chs[i] = c;
                        String target = String.valueOf(chs);


                        if (wordList.contains(target)) {
                        	adj.get(u).add(mapping.get(target));
                        	temp.add(target);	
                        }
                        chs[i] = old;
                        
                    }
                }
            }
            wordList.removeAll(temp);
            set = temp;
        }    
        return new Graph(vertices, adj);

    }

    private boolean isAdjacent(String string1, String string2) {
        int diff = 0;
        for (int i = 0; i < string2.length(); i++) {
            if (string1.charAt(i) != string2.charAt(i))
                diff++;
            if (diff > 1) {
                return false;
            }
        }
        return diff == 1;
    }
}

class Vertex {
    public static final int WHITE = 0;
    public static final int GRAY = 1;
    public static final int BLACK = 2;
    private String key;
    private int color = WHITE;
    private int d = -1;

    public Vertex(String key) {
        setKey(key);
    }
    public int getColor() {
        return color;
    }
    public void setColor(int color) {
        this.color = color;
    }
    public int getD() {
        return d;
    }
    public void setD(int d) {
        this.d = d;
    }
    public String getKey() {
        return key;
    }
    public void setKey(String key) {
        this.key= key;
    }

}

class Graph {
    private Vertex[] vertices;
    private HashMap<Vertex, ArrayList<Vertex>> adj;

    public Graph(Vertex[] vertices, HashMap<Vertex, ArrayList<Vertex>> adj) {
        this.vertices = vertices;
        this.adj = adj;
    }

    private void bfs(Vertex s) {
        s.setD(0);
        s.setColor(Vertex.GRAY);
        Queue<Vertex> q = new LinkedList<Vertex>();
        q.add(s);
        while (q.size() != 0) {
            Vertex u = q.remove();
            for (Vertex v : adj.get(u)) {
                if (v.getColor() == Vertex.WHITE) {
                    v.setD(u.getD() + 1);
                    v.setColor(Vertex.GRAY);
                    q.add(v);
                }
            }
            u.setColor(Vertex.BLACK);
        }
    }

    public List<List<String>> findAllPaths(Vertex s, Vertex t) {
        bfs(s);
        ArrayList<List<String>> solution = new ArrayList<List<String>>();
        ArrayList<String> partial = new ArrayList<String>();
        findAllPathsAux(s, t, solution, partial);
        return solution;
    }

    private void findAllPathsAux(Vertex u, Vertex t, List<List<String>> solution, ArrayList<String> partial) {
        if (u == t) {
            partial.add(t.getKey());
            solution.add((ArrayList<String>) partial.clone());
            partial.remove(partial.size() - 1);
        } else if (u.getD() < t.getD()) {
            partial.add(u.getKey());
            for (Vertex v: adj.get(u)) {
                if (v.getD() == u.getD() + 1) {
                    findAllPathsAux(v, t, solution, partial);
                }
            }
            partial.remove(partial.size() - 1);
        }
    }
}

   