# A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it equals the query. (We may insert each character at any position, and may insert 0 characters.)
#
# Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true if and only if queries[i] matches the pattern.
#
#  
#
# Example 1:
#
#
# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
# Output: [true,false,true,true,false]
# Explanation: 
# "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
# "FootBall" can be generated like this "F" + "oot" + "B" + "all".
# "FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
#
# Example 2:
#
#
# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
# Output: [true,false,true,false,false]
# Explanation: 
# "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
# "FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
#
#
# Example 3:
#
#
# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
# Output: [false,true,false,false,false]
# Explanation: 
# "FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".
#
#
#  
#
# Note:
#
#
# 	1 <= queries.length <= 100
# 	1 <= queries[i].length <= 100
# 	1 <= pattern.length <= 100
# 	All strings consists only of lower and upper case English letters.
#
#


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for q in queries:
            dp = [[ False ] * (len(pattern) + 1) for _ in range(len(q) + 1)]
            dp[0][0] = True
            for i in range(len(q)):
                if q[i].islower():
                    dp[i + 1][0] = True
                else:
                    break
            for i in range(1, len(q) + 1):
                for j in range(1, len(pattern) + 1):
                    if q[i - 1] == pattern[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                        continue
                    elif q[i - 1].islower():
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = False
                    
                    
            res.append(dp[len(q)][len(pattern)])
        return res
                
        
