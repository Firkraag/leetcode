class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.val2index = dict()
        self.index2val = dict()

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.val2index:
            self.size += 1
            self.index2val[self.size] = val
            self.val2index[val] = {self.size}
            return True
        else:
            self.size += 1
            self.val2index[val].add(self.size)
            self.index2val[self.size] = val
            return False
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.val2index:
            #print "start remove ", self.index2val, self.val2index
            s = self.val2index[val]
            index = next(iter(s))
            lastVal = self.index2val[self.size]
            self.index2val[index] = lastVal
            self.index2val.pop(self.size)
            self.val2index[lastVal].discard(self.size)
            self.val2index[lastVal].add(index)
            s.discard(index)
            if len(s) == 0:
                del self.val2index[val]
            self.size -= 1
            #print "end remove ", self.index2val, self.val2index
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        if self.size <= 0:
            return 0
        else:
            from random import randint
            index = randint(1, self.size)
            return self.index2val[index]        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()