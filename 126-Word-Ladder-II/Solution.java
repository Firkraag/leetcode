public class Solution {
    public List<List<String>> findLadders(String beginWord, String endWord, Set<String> wordList) {
        int diff = 0;
        for (int i = 0; i < beginWord.length(); i++) {
            if (beginWord.charAt(i) != endWord.charAt(i))
                diff++;
        }
        if (diff == 0)
            return 1;
        else if (diff == 1)
            return 2;
        else
        {
            Vertex source = new Vertex();
            Vertex sink = new Vertex();
            Graph graph = constructGraph(beginWord, endWord, wordList, source, sink);
            graph.bfs(source);
            if (sink.getD() == -1)
                return 0;
            else
                return sink.getD() + 1;
        }
    }
    
    private Graph constructGraph(String beginWord, String endWord, Set<String> wordList, Vertex source, Vertex sink) {
        int n = wordList.size();
        List<String> list = new ArrayList<String>();
        list.addAll(wordList);
        HashMap<Vertex, ArrayList<Vertex>> adj = new HashMap<Vertex, ArrayList<Vertex>>();
        Vertex[] vertices = new Vertex[n + 2];
        for (int i = 0; i < n; i++)
        {
            vertices[i] = new Vertex();
            adj.put(vertices[i], new ArrayList<Vertex>());
        }
        vertices[n] = source;
        vertices[n + 1] = sink;
        ArrayList<Vertex> sourceList = new ArrayList<Vertex>();
        ArrayList<Vertex> sinkList = new ArrayList<Vertex>();
        adj.put(source, sourceList);
        adj.put(sink, sinkList);
        for (int i = 0; i < n; i++)
        {
            Vertex node1 = vertices[i];
            ArrayList<Vertex> l1 = adj.get(node1);
            for (int j = i + 1; j < n; j++)
                if (isAdjacent(list.get(i), list.get(j)))
                {
                    Vertex node2 = vertices[j];
                    ArrayList<Vertex> l2 = adj.get(node2);
                    l1.add(node2);
                    l2.add(node1);
                }
            if (isAdjacent(list.get(i), beginWord))
            {
                l1.add(source);
                sourceList.add(node1);
            }
            if (isAdjacent(list.get(i), endWord))
            {
                l1.add(sink);
                sinkList.add(node1);
            }
        }
        return new Graph(vertices, adj);
    }

    private boolean isAdjacent(String string1, String string2) {
        int diff = 0;
        for (int i = 0; i < string2.length(); i++) {
            if (string1.charAt(i) != string2.charAt(i))
                diff++;
        }
        return diff == 1;
    }

}

    
class Vertex {
    public static final int WHITE = 0;
    public static final int GRAY = 1;
    public static final int BLACK = 2;
    private int color = WHITE;
    private int d = -1;
    
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
    
}

class Graph {
    private Vertex[] vertices;
    private HashMap<Vertex, ArrayList<Vertex>> adj;
    
    public Graph(Vertex[] vertices, HashMap<Vertex, ArrayList<Vertex>> adj) {
        this.vertices = vertices;
        this.adj = adj;
    }
    
    public void bfs(Vertex s) {
       s.setD(0);
       s.setColor(Vertex.GRAY);
       Queue<Vertex> q = new LinkedList<Vertex>();
       q.add(s);
       while (q.size() != 0)
       {
           Vertex u = q.remove();
           for (Vertex v : adj.get(u)) {
               if (v.getColor() == Vertex.WHITE)
               {
                   v.setD(u.getD() + 1);
                   v.setColor(Vertex.GRAY);
                   q.add(v);
               }
           }
           u.setColor(Vertex.BLACK);
       }
    }
}
