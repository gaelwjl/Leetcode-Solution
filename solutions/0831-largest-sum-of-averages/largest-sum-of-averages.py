# We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?
#
# Note that our partition must use every number in A, and that scores are not necessarily integers.
#
#
# Example:
# Input: 
# A = [9,1,2,3,9]
# K = 3
# Output: 20
# Explanation: 
# The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
# We could have also partitioned A into [9, 1], [2], [3, 9], for example.
# That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
#
#
#  
#
# Note: 
#
#
# 	1 <= A.length <= 100.
# 	1 <= A[i] <= 10000.
# 	1 <= K <= A.length.
# 	Answers within 10^-6 of the correct answer will be accepted as correct.
#
#


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        presum = [0]
        for a in A:
            presum.append(presum[-1] + a)
        @lru_cache(None)
        def dfs(i, K):
            if K == 1:
                return presum[i + 1] / (i + 1)
            if i + 1 == K:
                return presum[i + 1]
            ans = 0
            for j in range(i):
                ans = max(ans, dfs(j, K - 1) + (presum[i + 1] - presum[j + 1])/(i - j))
            print(i, K, ans)
            return ans
        return dfs(len(A) - 1, K)
