# Given an array of integers arr and two integers k and threshold.
#
# Return the number of sub-arrays of size k and average greater than or equal to threshold.
#
#  
# Example 1:
#
#
# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
#
#
# Example 2:
#
#
# Input: arr = [1,1,1,1,1], k = 1, threshold = 0
# Output: 5
#
#
# Example 3:
#
#
# Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
# Output: 6
# Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
#
#
# Example 4:
#
#
# Input: arr = [7,7,7,7,7,7,7], k = 7, threshold = 7
# Output: 1
#
#
# Example 5:
#
#
# Input: arr = [4,4,4,4], k = 4, threshold = 1
# Output: 1
#
#
#  
# Constraints:
#
#
# 	1 <= arr.length <= 10^5
# 	1 <= arr[i] <= 10^4
# 	1 <= k <= arr.length
# 	0 <= threshold <= 10^4
#


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        tempSum = sum(arr[0:k])
        n = len(arr)
        res = 0
        i = 0
        crit = threshold * k
        if tempSum >= crit: res += 1
        while i < (n - k):
            tempSum -= arr[i]
            tempSum += arr[i + k]
            if tempSum >= crit: res += 1
            i += 1
        return res