class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        justify = []
        i = 0
        n = len(words)
        if n == 0:
            return []
        while True:
            start = i
            length = len(words[i])
            lengthOfWord = len(words[i])
            i += 1
            while i < n:
                if length + len(words[i]) + 1 <= maxWidth:
                    length += 1 + len(words[i])
                    lengthOfWord += len(words[i])
                    i += 1
                else:
                    end = i - 1
                    break
            if i >= n:
                justify.append(' '.join(words[start:i]) + ' ' * (maxWidth - length)) 
                break
            else:
                numOfSpace = end - start
                if numOfSpace == 0:
                    justify.append(words[start] + ' ' * (maxWidth - len(words[start])))
                else:
                    averageSpace = (maxWidth - lengthOfWord) / numOfSpace
                    moreSpacePart = (maxWidth - lengthOfWord) % numOfSpace
                    temp = []
                    for j in range(start, start + moreSpacePart):
                        temp.append(words[j])
                        temp.append(' ' * (averageSpace + 1))
                    for j in range(start + moreSpacePart, end):
                        temp.append(words[j])
                        temp.append(' ' * averageSpace)
                    temp.append(words[end])
                    justify.append(''.join(temp))
            #print justify
        return justify        
            