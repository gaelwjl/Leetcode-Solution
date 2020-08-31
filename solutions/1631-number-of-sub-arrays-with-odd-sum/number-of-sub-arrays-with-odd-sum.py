# Given an array of integers arr. Return the number of sub-arrays with odd sum.
#
# As the answer may grow large, the answer must be computed modulo 10^9 + 7.
#
#  
# Example 1:
#
#
# Input: arr = [1,3,5]
# Output: 4
# Explanation: All sub-arrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
# All sub-arrays sum are [1,4,9,3,8,5].
# Odd sums are [1,9,3,5] so the answer is 4.
#
#
# Example 2:
#
#
# Input: arr = [2,4,6]
# Output: 0
# Explanation: All sub-arrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
# All sub-arrays sum are [2,6,12,4,10,6].
# All sub-arrays have even sum and the answer is 0.
#
#
# Example 3:
#
#
# Input: arr = [1,2,3,4,5,6,7]
# Output: 16
#
#
# Example 4:
#
#
# Input: arr = [100,100,99,99]
# Output: 4
#
#
# Example 5:
#
#
# Input: arr = [7]
# Output: 1
#
#
#  
# Constraints:
#
#
# 	1 <= arr.length <= 10^5
# 	1 <= arr[i] <= 100
#


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = int(1e9 + 7)
        nodds = [0 for _ in range(n + 1)]
        nevens = nodds[:]
        nevens[0] = 0
        for i in range(1, n + 1):
            if arr[i - 1] % 2 == 0:
                nodds[i] = nodds[i - 1]
                nevens[i] = (nevens[i - 1] + 1) % MOD
            else:
                nodds[i] = (nevens[i - 1] + 1) % MOD
                nevens[i] = nodds[i - 1]
        return sum(nodds[1:]) % MOD
