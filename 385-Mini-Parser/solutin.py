# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        tokenList = self.parse(s)
        if len(tokenList) == 1:
            return NestedInteger(tokenList[0])
        else:
            ni, index = self.process(tokenList, 0)
            return ni
            
    def process(self, tokenList, start):
        i = start + 1
        ni = NestedInteger()
        l = ni.getList()
        while tokenList[i] != ']':
            token = tokenList[i]
            if token == '[':
                element, index = self.process(tokenList, i)
                i = index + 1
                l.append(element)
            else:
                l.append(NestedInteger(token))
                i += 1
        return ni, i
        
    def parse(self, s):
        numeric = set("12345678090")
        tokenList = []
        i = 0
        while i < len(s):
            char = s[i]
            if char == '[' or char == ']':
                tokenList.append(s[i])
                i += 1
            elif char == ',':
                i += 1
            elif char == '-':
                i += 1
                number = 0
                
                while i < len(s) and s[i] in numeric:
                    number = number * 10 + int(s[i])
                    i += 1
                tokenList.append(number * -1)
            else:
                number = 0
                while i < len(s) and s[i] in numeric:
                    number = number * 10 + int(s[i])
                    i += 1
                tokenList.append(number)
        return tokenList
        
