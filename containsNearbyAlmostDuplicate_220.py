class Node(object):
    def __init__(self, key, p = None, left = None, right = None):
        self.key = key
        self.p = p
        self.left = left
        self.right = right
    def minimum(self):
        x = self
        while x.left != None:
            x = x.left
        return x
    def maximum(self):
        x = self
        while x.right != None:
            x = x.right
        return x
    
    def successor(self):
        x = self
        if x.right != None:
            return x.right.minimum()
        else:
            while x.p != None and x.p.right == x:
                x = x.p
            return x.p
    def predecessor(self):
        x = self
        if x.left != None:
            return x.left.maximum()
        else:
            while x.p != None and x.p.left == x:
                x = x.p
            return x.p

class Tree(object):
    def __init__(self, values = None):
        self.root = None
        if isinstance(values, list):
            for i in values:
                self.insert(Node(i, None, None, None))
        elif values != None:
            self.insert(Node(values, None, None, None))
    def minimum(self):
        return self.root.minimum()
    def insert(self, node):
        y = None
        x = self.root
        while x != None:
            y = x
            if node.key <= x.key:
                x = x.left
            else:
                x = x.right
        node.p = y
        if y == None:
            self.root = node
        elif node.key <= y.key:
            y.left = node
        else:
            y.right = node
    def transplant(self, u, v):
        if u.p == None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v != None:
            v.p = u.p
    def delete(self, z):
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = z.right.minimum()
            if y.p != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
    
    def left_rotate(self, x):
        y = x.right
        z = y.left
        p = x.p
        x.right = z
        x.p = y
        y.left = x
        y.p = p
        if z != None:
            z.p = x
        if p == None:
            self.root = y
        elif p.left == x:
            p.left = y
        else:
            p.right = y

    def right_rotate(self, y):
        x = y.left
        z = x.right
        p = y.p
        y.left = z
        y.p = x
        x.right = y
        x.p = p
        if z != None:
            z.p = y
        if p == None:
            self.root = x
        elif p.left == y:
            p.left = x
        else:
            p.right = x
    
    def changeRoot(self, node):
        #print "enter"
        while node.p != None:
            p = node.p
            if p.left == node:
                self.right_rotate(p)
            else:
                self.left_rotate(p)
        #print "exit"
        
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        n = len(nums)
        mapping = [None] * n
        tree = Tree()
        pos = 0
        while pos < min(k + 1, n):
            node = Node(nums[pos])
            mapping[pos] = node
            tree.insert(node)
            pos += 1
        for i in range(n - 1):
            node = mapping[i]
            predecessor = node.predecessor()
            successor = node.successor()
            if (predecessor != None and node.key - predecessor.key <= t) or (successor != None and successor.key - node.key <= t):
                return True
            else:
                if pos < n:
                    newNode = Node(nums[pos])
                    mapping[pos] = newNode
                    tree.insert(newNode)
                    pos += 1
                tree.delete(node)
                tree.changeRoot(mapping[i + 1])
                
        return False
