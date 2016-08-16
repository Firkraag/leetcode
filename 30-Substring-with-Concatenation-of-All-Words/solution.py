class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if (len(s) == 0 or len(words) == 0 or len(words[0]) == 0):
            return []
        print len(s)
        print len(words), len(words[0])
        n = len(s)
        wordLength = len(words[0])
        totalLength = wordLength * len(words) 
        result = []
        from collections import Counter
        counter = Counter(words)
        c = 0
        for k in range(wordLength):
            if k + totalLength - 1 > n - 1:
                break
            number = counter.copy()
            size = len(number)
            start = k
            i = k
            while i < n:
                word = s[i : i + wordLength]
                if word not in number:
                    i += wordLength
                    if n - i < totalLength:
                        break
                    else:
                        number = counter.copy()
                        size = len(number)
                        start = i
                else:
                    value = number[word]
                    if value > 1:
                        number[word] -= 1
                    elif value == 1:
                        number[word] = 0
                        size -= 1
                        if size == 0:
                            result.append(start)
                            number[s[start:start + wordLength]] = 1
                            start += wordLength
                            size = 1
                    else:
                        j = start
                        while s[j : j + wordLength] != word:
                            startWord = s[j : j + wordLength]
                            value = number[startWord]
                            if value == 0:
                                size += 1
                            number[startWord] = value + 1
                            j += wordLength
                        start = j + wordLength
                    i += wordLength
        return result