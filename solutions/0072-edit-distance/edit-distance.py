# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
#
# 	Insert a character
# 	Delete a character
# 	Replace a character
#
#
# Example 1:
#
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#
#
# Example 2:
#
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#
#


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1) + 1
        m = len(word2) + 1
        mini = [[ 0 for _ in range(m)] for _ in range(n)]
        mini[0][0] = 0
        for i in range(1, n):
            mini[i][0] = i
        for j in range(1, m):
            mini[0][j] = j
        for i in range(1, n):
            for j in range(1, m):
                if word1[i - 1] == word2[j - 1]:
                    mini[i][j] = mini[i - 1][j - 1]
                else:
                    mini[i][j] = min(mini[i - 1][j], mini[i - 1][j - 1], mini[i][j - 1]) + 1
        return mini[n - 1][m - 1]
        
