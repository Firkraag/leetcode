class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        import fractions
        if z > y + x:
            return False
        gcd = fractions.gcd(x, y)
        if gcd == 0:
            if x == z or y == z:
                return True
            else:
                return False
        elif z % gcd == 0:
            return True
        else:
            return False
    
