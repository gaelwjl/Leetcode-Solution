# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# Example:
#
#
# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]
#
#


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def ispalin(s):
            for i in range(len(s) // 2):
                if s[i] != s[len(s) -1 - i]:
                    return False
            return True
        n = len(s)
        dp = [[] for _ in range(n + 1)]
        def helper(s):
            for i in range(n + 1):
                for j in range(i + 1, n + 1):
                    if (not ispalin(s[i:j])):
                        pass
                    else:
                        if len(dp[i]) == 0:
                            dp[j].append([s[i:j]])
                        else:
                            for x in dp[i]:
                                tmp = x + [s[i:j]]
                                dp[j].append(tmp)
        helper(s)
        return dp[n]
