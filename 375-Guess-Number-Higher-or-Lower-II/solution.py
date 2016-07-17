class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        money = [[None] * (n  + 1) for i in range(n + 1)]
        self.getMoneyAmountAux(1, n, money)
        return money[1][n]
    
    def getMoneyAmountAux(self, p, r, money):
        if p > r:
            return 0
        elif money[p][r] != None:
            return money[p][r]
        elif p == r:
            money[p][r] = 0
            return 0
        elif p + 1 == r:
            money[p][r] = p
            return p
        else:
            gurantee = float("Inf")
            for i in range(p, r + 1):
                gurantee = min(gurantee, max(i + self.getMoneyAmountAux(p, i - 1, money), i + self.getMoneyAmountAux(i + 1, r, money)))
            money[p][r] = gurantee
            return gurantee