class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head. Note that the head is guanranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.nodeList = []
        node = head
        while node != None:
            self.nodeList.append(node)
            node = node.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        n = len(self.nodeList)
        from random import randint
        return self.nodeList[randint(0, n - 1)].val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
