class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.val2index = dict()
        self.index2val = dict()
        
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.val2index:
            self.size += 1
            self.index2val[self.size] = val
            self.val2index[val] = self.size
            return True
        else:
            return False
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.val2index:
            index = self.val2index[val]
            lastVal = self.index2val[self.size]
            self.index2val[index] = lastVal
            self.val2index[lastVal] = index
            self.val2index.pop(val)
            self.index2val.pop(self.size)
            self.size -= 1
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.size <= 0:
            return 0
        else:
            from random import randint
            index = randint(1, self.size)
            return self.index2val[index]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()