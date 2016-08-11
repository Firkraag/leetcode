class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        for char, counter in c1.iteritems():
            if not (char in c2 and counter <= c2[char]):
                return False
        return True