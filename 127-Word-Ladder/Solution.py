class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        from string import ascii_lowercase
        beginSet = {beginWord}
        endSet = {endWord}
        wordList.discard(beginWord)
        length = 1
        while len(beginSet) != 0 and len(endSet) != 0:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            tmp = set()
            for word in beginSet:
                for i in range(len(word)):
                    for c in ascii_lowercase:
                        newWord = word[:i] + c + word[i + 1:]
                        if newWord in endSet:
                            return length + 1
                        elif newWord in wordList:
                            wordList.discard(newWord)
                            tmp.add(newWord)  
            beginSet = tmp
            length += 1
        return 0
        
        
