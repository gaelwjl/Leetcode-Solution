# Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.
#
# (A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)
#
#  
#
# Example 1:
#
#
# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"
# Explanation: 
# str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
# str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
# The answer provided is the shortest such string that satisfies these properties.
#
#
#  
#
# Note:
#
#
# 	1 <= str1.length, str2.length <= 1000
# 	str1 and str2 consist of lowercase English letters.
#
#


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        dp = [[0]*(m + 1) for _ in range(n + 1)]
        res = []
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        def dfs(i, j, res):
            if i == 0 and j == 0:
                return 
            if dp[i][j] == dp[i - 1][j - 1] + 1 and str1[i - 1] == str2[j - 1]:
                res.append(str1[i - 1])
                dfs(i - 1, j - 1, res)
            elif i >= 1 and dp[i][j] == dp[i - 1][j]:
                res.append(str1[i - 1])
                dfs(i - 1, j, res)
            elif j >= 1 and dp[i][j] == dp[i][j - 1]:
                res.append(str2[j - 1])
                dfs(i, j - 1, res)
        dfs(n, m, res)
        return "".join(res[::-1])
