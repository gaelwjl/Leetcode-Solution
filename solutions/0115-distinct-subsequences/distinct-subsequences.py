# Given a string S and a string T, count the number of distinct subsequences of S which equals T.
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
# It's guaranteed the answer fits on a 32-bit signed integer.
#
# Example 1:
#
#
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
#
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
#
#
# Example 2:
#
#
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
#
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^
#
#


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def helper(i ,j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i < j:
                return 0
            if j == -1:
                return 1
            ans = 0
            if s[i] == t[j]:
                ans += helper(i - 1, j - 1)
            ans += helper(i - 1, j)
            memo[(i, j)] = ans
            return memo[(i, j)]
        tmp = helper(len(s) - 1, len(t) - 1)
        return tmp
