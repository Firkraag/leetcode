class Node(object):
    def __init__(self, index):
        self.index = index
        self.p = self
        self.rank = 0
        self.flip = True
        self.set = set()
        self.set.add(self)
    def union(self, y):
        p1 = self.find_set()
        p2 = y.find_set()
        if p1 != p2:
            return p1.link(p2)
    def link(self, y):
        x = self
        if x.rank > y.rank:
            y.p = x
            x.flip = x.flip and y.flip
            x.set.update(y.set)
            y.set = None
            return y
        else:
            x.p = y
            y.flip = x.flip and y.flip
            if x.rank == y.rank:
                y.rank = y.rank + 1
            y.set.update(x.set)
            x.set = None
            return x
    def find_set(self):
        x = self
        if x != x.p:
            x.p = x.p.find_set()
        return x.p
        
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        if n == 0:
            return
        nodes = dict()
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    node1 = Node((i, j))
                    nodes[(i,j)] = node1
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        node1.flip = False
                    if i > 0 and board[i - 1][j] == 'O':
                        node1.union(nodes[(i - 1, j)])
                    if j > 0 and board[i][j - 1] == 'O':
                        node1.union(nodes[(i, j - 1)])
        for index, node in nodes.iteritems():
            i, j = index
            p = node.find_set()
            #print node.index, p.index
            if p.flip and board[i][j] == 'O':
                self.flipSubset(p, board)
                
    def flipSubset(self, p, board):
        for node in p.set:
            i, j = node.index
            board[i][j] = 'X'
  
