class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        import heapq
        self.stack = []
        self.heap = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        l = [x, False]
        self.stack.append(l)
        heapq.heappush(self.heap, l)

    def pop(self):
        """
        :rtype: void
        """
        l = self.stack.pop()
        l[1] = True

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        while self.heap[0][1]:
            heapq.heappop(self.heap)
        return self.heap[0][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
