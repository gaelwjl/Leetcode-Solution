# You are given a string s containing lowercase letters and an integer k. You need to :
#
#
# 	First, change some characters of s to other lowercase English letters.
# 	Then divide s into k non-empty disjoint substrings such that each substring is palindrome.
#
#
# Return the minimal number of characters that you need to change to divide the string.
#
#  
# Example 1:
#
#
# Input: s = "abc", k = 2
# Output: 1
# Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.
#
#
# Example 2:
#
#
# Input: s = "aabbc", k = 3
# Output: 0
# Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.
#
# Example 3:
#
#
# Input: s = "leetcode", k = 8
# Output: 0
#
#
#  
# Constraints:
#
#
# 	1 <= k <= s.length <= 100.
# 	s only contains lowercase English letters.
#


class Solution:
    def palindromePartition(self, s: str, K: int) -> int:
        n = len(s)
        def cost(i, j):
            mid = (i + j) // 2
            c = 0
            for k in range(i, mid + 1):
                if s[k] != s[i + j - k]:
                    c += 1
            return c
        
        @lru_cache(None)
        def dfs(i, k):
            if k == 1:
                return cost(i, len(s) - 1)
            ans = float('inf')
            for j in range(i, n):
                ans = min(ans, cost(i, j) + dfs(j + 1, k - 1))
            return ans
        return dfs(0, K)
