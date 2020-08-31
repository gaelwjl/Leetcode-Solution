# Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
# Input:
#
#
# "bbbab"
#
# Output:
#
#
# 4
#
# One possible longest palindromic subsequence is "bbbb".
#
#  
#
# Example 2:
# Input:
#
#
# "cbbd"
#
# Output:
#
#
# 2
#
# One possible longest palindromic subsequence is "bb".
#  
# Constraints:
#
#
# 	1 <= s.length <= 1000
# 	s consists only of lowercase English letters.
#
#


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        @lru_cache(None)
        def dfs(i, j):
            if i == j:
                return 1
            if j == i + 1:
                if s[i] == s[i + 1]:
                    return 2
                else:
                    return 1
            if s[i] == s[j]:
                return dfs(i + 1, j - 1) + 2
            else:
                return max(dfs(i, j - 1), dfs(i + 1, j))
        return dfs(0, len(s) - 1)
