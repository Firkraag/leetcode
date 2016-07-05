class Node {
    private long key;
    private Node p = null;
    private Node left = null;
    private Node right = null;
    
    public Node(long key) {
        setKey(key);
    }
    
    public long getKey() {
        return key;
    }
    
    public void setKey(long key) {
        this.key = key;
    }
    
    public Node getP() {
        return p;
    }
    public void setP(Node p) {
        this.p = p;
    }
    public Node getLeft() {
        return left;
    }
    public void setLeft(Node left) {
        this.left = left;
    }
    public Node getRight() {
        return right;
    }
    public void setRight(Node right) {
        this.right = right;
    }
    public Node minimum() {
        Node x = this;
        while (x.getLeft() != null)
            x = x.getLeft();
        return x;
    }
    public Node maximum() {
        Node x = this;
        while (x.getRight() != null)
            x = x.getRight();
        return x;
    }
    public Node successor() {
        Node x = this;
        if (x.getRight() != null)
            return x.getRight().minimum();
        else {
            while (x.getP() != null && x.getP().getRight() == x)
                x = x.getP();
            return x.getP();
        }
    }
    public Node predecessor() {
        Node x = this;
        if (x.getLeft() != null)
            return x.getLeft().maximum();
        else {
            while (x.getP() != null && x.getP().getLeft() == x)
                x = x.getP();
            return x.getP();
        }
    }
}

class Tree {
    private Node root = null;
    
    public Node minimum() {
        return root.minimum();
    }
    public void insert(Node node) {
        Node y = null;
        Node x = root;
        while (x != null)
        {
            y = x;
            if (node.getKey() <= x.getKey())
                x = x.getLeft();
            else
                x = x.getRight();
        }
        node.setP(y);
        if (y == null)
            root = node;
        else if (node.getKey() <= y.getKey())
            y.setLeft(node);
        else
            y.setRight(node);
    }
    private void transplant(Node u, Node v) {
        if (u.getP() == null)
            root = v;
        else if (u == u.getP().getLeft())
            u.getP().setLeft(v);
        else
            u.getP().setRight(v);
        
        if (v != null)
            v.setP(u.getP());
    }
    public void delete(Node z) {
        if (z.getLeft() == null) {
            transplant(z, z.getRight());
        }
        else if (z.getRight() == null)
            transplant(z, z.getLeft());
        else {
            Node y = z.getRight().minimum();
            if (y.getP() != z)
            {
                transplant(y, y.getRight());
                y.setRight(z.getRight());
                y.getRight().setP(y);
            }
            transplant(z, y);
            y.setLeft(z.getLeft());
            y.getLeft().setP(y);
        }
    }
    private void leftRotate(Node x) {
        Node y = x.getRight();
        Node z = y.getLeft();
        Node p = x.getP();
        
        x.setRight(z);
        x.setP(y);
        y.setLeft(x);
        y.setP(p);
        if (z != null)
            z.setP(x);
        if (p == null)
            root = y;
        else if (p.getLeft() == x)
            p.setLeft(y);
        else
            p.setRight(y);
    }
    public void rightRotate(Node y) {
        Node x = y.getLeft();
        Node z = x.getRight();
        Node p = y.getP();
        y.setLeft(z);
        y.setP(x);
        x.setRight(y);
        x.setP(p);
        if (z != null)
            z.setP(y);
        if (p == null)
            root = x;
        else if (p.getLeft() == y)
            p.setLeft(x);
        else
            p.setRight(x);
    }
    public void changeRoot(Node node) {
        while (node.getP() != null)
        {
            Node p = node.getP();
            if (p.getLeft() == node)
                rightRotate(p);
            else
                leftRotate(p);
        }
    }
    
}

   
   
public class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        int n = nums.length;
        Node[] mappings = new Node[n];
        Tree tree = new Tree();
        int pos = 0;
        while (pos < Math.min(k + 1, n))
        {
            Node node = new Node(nums[pos]);
            mappings[pos] = node;
            tree.insert(node);
            pos++;
        }
        for (int i = 0; i < n - 1; i++) {
            Node node = mappings[i];
            Node predecessor = node.predecessor();
            Node successor = node.successor();
            if ((predecessor != null && node.getKey() - predecessor.getKey() <= t) || (successor != null && successor.getKey() - node.getKey() <= t))
                return true;
            else {
                if (pos < n)
                {
                    Node newNode = new Node(nums[pos]);
                    mappings[pos] = newNode;
                    tree.insert(newNode);
                    pos += 1;
                }
                tree.delete(node);
                tree.changeRoot(mappings[i + 1]);
            }
        }
        return false;    
    }
}
