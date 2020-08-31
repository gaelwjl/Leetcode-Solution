# Given a string s. In one step you can insert any character at any index of the string.
#
# Return the minimum number of steps to make s palindrome.
#
# A Palindrome String is one that reads the same backward as well as forward.
#
#  
# Example 1:
#
#
# Input: s = "zzazz"
# Output: 0
# Explanation: The string "zzazz" is already palindrome we don't need any insertions.
#
#
# Example 2:
#
#
# Input: s = "mbadm"
# Output: 2
# Explanation: String can be "mbdadbm" or "mdbabdm".
#
#
# Example 3:
#
#
# Input: s = "leetcode"
# Output: 5
# Explanation: Inserting 5 characters the string becomes "leetcodocteel".
#
#
# Example 4:
#
#
# Input: s = "g"
# Output: 0
#
#
# Example 5:
#
#
# Input: s = "no"
# Output: 1
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 500
# 	All characters of s are lower case English letters.
#


class Solution:
    def minInsertions(self, s: str) -> int:
        return len(s) - self.longestCS(s, s[::-1])
        
    def longestCS(self, x, y):
        dp = [[0]*(len(x) + 1) for _ in range(len(y) + 1)]
        for i in range(1, len(x) + 1):
            for j in range(1, len(y) + 1):
                if x[i - 1] == y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[len(y)][len(x)]
