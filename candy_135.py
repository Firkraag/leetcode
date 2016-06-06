#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n == 1:
            return 1
        candies = [1] * n
        i = 0
        requirement = 1
        while i < n - 1:
            if ratings[i] == ratings[i + 1]:
                start = i
                while i < n - 1 and ratings[i] == ratings[i + 1]:
                    i += 1
                end = i
                candies[start] = requirement
                for j in range(start + 1, end):
                    candies[j] = 1
                requirement = 1
            elif ratings[i] < ratings[i + 1]:
                start = i
                while i < n - 1 and ratings[i] < ratings[i + 1]:
                    i += 1
                end = i
                candies[start] = 1
                for j in range(start, end):
                    candies[j] = j - start + 1
                requirement = end - start + 1
            else:
                start = i
                while i < n - 1 and ratings[i] > ratings[i + 1]:
                    i += 1
                end = i
                candies[start] = max(requirement, end - start + 1)
                length = end - start
                for j in range(start + 1, end):
                    candies[j] = length
                    length -= 1
                requirement = 1
        candies[n - 1] = requirement
        #print candies
        return sum(candies)
