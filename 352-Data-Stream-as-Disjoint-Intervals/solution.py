# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = Tree()

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        self.tree.insert(val)

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        intervals = []
        self.tree.getIntervals(intervals)
        return intervals

class Node(object):
    
    def __init__(self, start, end, p = None):
        self.interval = Interval(start, end)
        self.p = p
        self.left = None
        self.right = None
        
    def getIntervals(self, intervals):
        if self.left != None:
            self.left.getIntervals(intervals)
        intervals.append(self.interval)
        if self.right != None:
            self.right.getIntervals(intervals)
            
    def insert(self, val):
        start = self.interval.start
        end = self.interval.end
        if val < start:
            if val + 1 == start:
                if self.left == None:
                    self.interval.start = val
                else:
                    node = self.left.maximum()
                    start = node.interval.start
                    end = node.interval.end
                    if end + 1 == val:
                        if node.p == self:
                            self.left = node.left
                            if node.left != None:
                                node.left.p = self
                        else:
                            node.p.right = node.left
                            if node.left != None:
                                node.left.p = node.p
                        self.interval.start = start
                    else:
                        self.interval.start = val
            elif self.left == None:
                node = Node(val, val, self)
                self.left = node
            else:
                self.left.insert(val)
        elif val > end:
            if end + 1 == val:
                if self.right == None:
                    self.interval.end = val
                else:
                    node = self.right.minimum()
                    start = node.interval.start
                    end = node.interval.end
                    if val + 1 == start:
                        if node.p == self:
                            self.right = node.right
                            if node.right != None:
                                node.right.p = self
                        else:
                            node.p.left = node.right
                            if node.right != None:
                                node.right.p = node.p
                        self.interval.end = end
                    else:
                        self.interval.end = val
            elif self.right == None:
                node = Node(val, val, self)
                self.right = node
            else:
                self.right.insert(val)
    
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
            
class Tree(object):
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if self.root == None:
            self.root = Node(val, val)
        else:
            self.root.insert(val)
    
    def getIntervals(self, intervals):
        if self.root != None:
            self.root.getIntervals(intervals)

        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)

# param_2 = obj.getIntervals()