class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.tree = SegmentTree(nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.tree.update(i, val)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.tree.getRangeSum(i, j)
        
class SegmentNode(object):
    def __init__(self, leftEnd, rightEnd, sum = None):
        self.leftEnd = leftEnd
        self.rightEnd = rightEnd
        self.sum = sum
        self.leftChild = None
        self.rightChild = None

    def getRangeSum(self, leftEnd, rightEnd):
        node = self
        if leftEnd <= node.leftEnd and node.rightEnd <= rightEnd:
            return node.sum
        elif rightEnd < node.leftEnd or leftEnd > node.rightEnd:
            return 0
        else:
            return node.leftChild.getRangeSum(leftEnd, rightEnd) + node.rightChild.getRangeSum(leftEnd, rightEnd)
            
    def update(self, index, value):
        node = self
        leftEnd = node.leftEnd
        rightEnd = node.rightEnd
        if leftEnd == rightEnd:
            node.sum = value
        else:
            mid = (leftEnd + rightEnd) / 2
            if index <= mid:
                node.leftChild.update(index, value)
            else:
                node.rightChild.update(index, value)
            node.sum = node.leftChild.sum + node.rightChild.sum
        return node.sum
        
class SegmentTree(object):
    def __init__(self, array):
        self.root = self.buildSegmentTree(array, 0, len(array) - 1)

    def buildSegmentTree(self, array, leftEnd, rightEnd):
        if leftEnd > rightEnd:
            return None
        elif leftEnd == rightEnd:
            return SegmentNode(leftEnd, rightEnd, array[leftEnd])
        else:
            node = SegmentNode(leftEnd, rightEnd)
            mid = (leftEnd + rightEnd) / 2
            leftChild = self.buildSegmentTree(array, leftEnd, mid)
            rightChild = self.buildSegmentTree(array, mid + 1, rightEnd)
            node.leftChild = leftChild
            node.rightChild = rightChild
            node.sum = leftChild.sum + rightChild.sum
            return node
    
    def getRangeSum(self, leftEnd, rightEnd):
        if self.root == None:
            return 0
        else:
            return self.root.getRangeSum(leftEnd, rightEnd)
    
    def update(self, index, value):
        if self.root == None:
            return None
        else:
            leftEnd = self.root.leftEnd
            rightEnd = self.root.rightEnd
            if leftEnd > index or rightEnd < index:
                return self.root.sum
            else:
                return self.root.update(index, value)
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
