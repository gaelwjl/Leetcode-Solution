#
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#
#
# For example, given n = 3, a solution set is:
#
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        memo = {}
        if n == 0:
            return [""]
        if n == 1:
            memo[1] = ["()"]
            return ["()"]
        if n in memo:
            return memo[n]
        res = []
        for k in range(n):
            for left in self.generateParenthesis(k):
                for right in self.generateParenthesis(n - 1 - k):
                    res.append("("+left+")"+ right)
        memo[n] = res
        return res
