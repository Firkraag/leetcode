class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        mappings = dict()
        n = len(words)
        result = set()
        for i in range(n):
            mappings[words[i]] = i
        for i in range(n):
            word = words[i]
            reverse = word[::-1]
            n = len(word)
            p = self.computeKMP(word)
            q = p[-1]
            while q > 0:
                string = word[:q - 1:-1]
                if string in mappings:
                    j = mappings[string]
                    result.add((j, i))
                q = p[q - 1]
            
            if reverse in mappings:
                j = mappings[reverse]
                if j != i:
                    result.add((j, i))

            p = self.computeKMP(reverse)
            q = p[-1]
            while q > 0:
                string = reverse[q:]
                if string in mappings:
                    j = mappings[string]
                    result.add((i, j))
                q = p[q - 1]
        return [list(pair) for pair in result]
    
    def computeKMP(self, word):
        word = word + "#" + word[::-1]
        m = len(word)
        p = [0] * m
        k = 0
        for q in range(1, m):
            while k > 0 and word[k] != word[q]:
                k = p[k - 1]
            if word[k] == word[q]:
                k += 1
            p[q] = k
        #print word, p
        return p