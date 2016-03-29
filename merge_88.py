#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[0:n] = nums2[0:n]
            return
        elif n == 0:
            return
        size = len(nums1)
        nums1[size - m:] = nums1[0:m]
        i = size - m
        j = 0
        k = 0
        while i < size and j < n:
            if nums1[i] <= nums2[j]:
                nums1[k] = nums1[i]
                k += 1
                i += 1
            else:
                nums1[k] = nums2[j]
                k += 1
                j += 1
        print i, j, k
        print nums1, nums2
        if i == size:
            nums1[k : m + n] = nums2[j:n]
        elif j == n:
            nums1[k : m + n] = nums1[i:size] 
