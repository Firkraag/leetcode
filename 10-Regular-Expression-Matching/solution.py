class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n1 = len(s)
        n2 = len(p)
        match = [[None] * n2 for i in range(n1)] 
        return self.isMatchAux(s, 0, n1 - 1, p, 0, n2 - 1, match)
        
    def isMatchAux(self, s, start1, end1, p, start2, end2, match):
        if start2 > end2:
            return start1 > end1
        elif start1 > end1:
            return p[start2:end2 + 1] == '.*'
        elif match[start1][start2] != None:
            return match[start1][start2]

        status = False
        if p[start1] != '.':
            if start2 < end2 and p[start2 + 1] == '*':
                if self.isMatchAux(s, start1, end1, p, start2 + 2, end2, match):
                    status = True
                else:
                    i = start1
                    while i <= end1 and s[i] == p[start2]:
                        if self.isMatchAux(s, i + 1, end1, p, start2 + 2, end2, match):
                            status = True
                            break
                        else:
                            i += 1
            else:
                status = (p[start2] == s[start1]) and self.isMatchAux(s, start1 + 1, end1, p, start2 + 1, end2, match)
        elif start2 < end2 and p[start2 + 1] == '*':
            for i in range(start1, end1 + 2):
                if self.isMatchAux(s, i, end1, p, start2 + 2, end2, match):
                    status = True
                    break
        else:
            status = self.isMatchAux(s, start1 + 1, end1, p, start2 + 1, end2, match)
        match[start1][start2] = status
        return status
