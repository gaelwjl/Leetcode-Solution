# -*- coding:utf-8 -*-


# This question is the same as "Max Chunks to Make Sorted" except the integers of the given array are not necessarily distinct, the input array could be up to length 2000, and the elements could be up to 10**8.
#
#
#
# Given an array arr of integers (not necessarily distinct), we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.
#
# What is the most number of chunks we could have made?
#
# Example 1:
#
#
# Input: arr = [5,4,3,2,1]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
#
#
# Example 2:
#
#
# Input: arr = [2,1,3,4,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [2, 1], [3, 4, 4].
# However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
#
#
# Note:
#
#
# 	arr will have length in range [1, 2000].
# 	arr[i] will be an integer in range [0, 10**8].
#
#
#  
#


class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        list_min = []
        list_max = []
        m = 0;
        big = 10 ** 8
        arr_inv = arr[::-1]
        for i in range(0, len(arr)):
            if arr[i] > m:
                list_max.append(arr[i])
                m = arr[i]
            else:
                list_max.append(m)

            if arr_inv[i] < big:
                list_min.append(arr_inv[i])
                big = arr_inv[i]
            else:
                list_min.append(big)
        list_min = list_min[::-1]
        res = 1
        for i in range(0, len(arr) - 1):
            if list_min[i + 1] >= list_max[i]:
                res += 1
        return res
        
            
