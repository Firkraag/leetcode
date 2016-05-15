#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 == 0 and n2 != 0:
            if n2 % 2 == 0:
                return (nums2[n2 / 2] + nums2[n2 / 2 - 1]) / 2.0
            else:
                return nums2[n2 / 2]
        elif n1 != 0 and n2 == 0:
            if n1 % 2 == 0:
                return (nums1[n1 / 2] + nums1[n1 / 2 - 1]) / 2.0
            else:
                return nums1[n1 / 2]
        if (n1 + n2) % 2 == 0:
            value1 = self.kthOfTwoSortedArrays(nums1, 0, n1 - 1, nums2, 0, n2 - 1, (n1 + n2) / 2)
            value2 = self.kthOfTwoSortedArrays(nums1, 0, n1 - 1, nums2, 0, n2 - 1, (n1 + n2) / 2 + 1)
            return (value1 + value2) / 2.0
        else:
            return self.kthOfTwoSortedArrays(nums1, 0, n1 - 1, nums2, 0, n2 - 1, (n1 + n2) / 2 + 1)
    
    def kthOfTwoSortedArrays(self, X, x_start, x_end, Y, y_start, y_end, k):
        if x_start > x_end:
            return Y[y_start + k - 1]
        if y_start > y_end:
            return X[x_start + k - 1]
        mid = (x_start + x_end) / 2
        index = self.binarySearch(Y, y_start, y_end, X[mid])
        size = mid - x_start + 1 + index - y_start + 1
        if size == k:
            return X[mid]
        elif size < k:
            return self.kthOfTwoSortedArrays(X, mid + 1, x_end, Y, index + 1, y_end, k - size)
        else:
            if mid == x_end and index == y_end:
                if k <= y_end - y_start + 1:
                    return Y[y_start + k - 1]
                else:
                    return X[x_end]
            else:
                return self.kthOfTwoSortedArrays(X, x_start, mid, Y, y_start, index, k)
    
    def binarySearch(self, array, low, high, value):
        while low <= high:
            mid = (low + high) / 2
            if array[mid] > value:
                high = mid - 1
            else:
                low = mid + 1
        return high
