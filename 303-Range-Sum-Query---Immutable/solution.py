class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.tree = SegmentTree(nums)

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


        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)