#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        remain = 0
        i = 0
        stop = [None] * n
        while i < n:
            tmp = remain + gas[i] - cost[i]
            if tmp >= 0:
                remain = tmp
                i += 1
            else:
                break
        if i == n:
            return 0
        else:
            stop[0] = (i, remain)
        for i in range(n - 1, 0, -1):
            if gas[i] < cost[i]:
                stop[i] = (i, 0)
            else:
                nextIndex = (i + 1) % n
                j = stop[nextIndex][0]
                if j == i:
                    return i
                else:
                    remain = stop[nextIndex][1] + gas[i] - cost[i]
                    while j != i:
                        tmp = remain + gas[j] - cost[j]
                        if tmp >= 0:
                            remain = tmp
                            j = (j + 1) % n
                        else:
                            break
                    if i == j:
                        return i
                    else:
                        stop[i] = (j, remain)
        return -1
