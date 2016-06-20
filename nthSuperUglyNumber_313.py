#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        from heapq import *
        ugly = [1] * n
        h = []
        for i in range(len(primes)):
            heappush(h, (primes[i], 1, primes[i]))
        for i in range(1, n):
            #print h
            while True:
                uglyNumber, uglyIndex, prime = heappop(h)
                if uglyNumber > ugly[i - 1]:
                    ugly[i] = uglyNumber
                    heappush(h, (prime * ugly[uglyIndex], uglyIndex + 1, prime))
                    break
                else:
                    heappush(h, (prime * ugly[uglyIndex], uglyIndex + 1, prime))

        return ugly[n - 1]
