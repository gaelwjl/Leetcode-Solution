# Given a balanced parentheses string S, compute the score of the string based on the following rule:
#
#
# 	() has score 1
# 	AB has score A + B, where A and B are balanced parentheses strings.
# 	(A) has score 2 * A, where A is a balanced parentheses string.
#
#
#  
#
#
# Example 1:
#
#
# Input: "()"
# Output: 1
#
#
#
# Example 2:
#
#
# Input: "(())"
# Output: 2
#
#
#
# Example 3:
#
#
# Input: "()()"
# Output: 2
#
#
#
# Example 4:
#
#
# Input: "(()(()))"
# Output: 6
#
#
#  
#
# Note:
#
#
# 	S is a balanced parentheses string, containing only ( and ).
# 	2 <= S.length <= 50
#
#
#
#
#
#


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        def score(s):
            if s == "":
                return 0
            if s == "()":
                return 1
            cnt = 1
            j = 1
            while j < len(s):
                if s[j] == '(':
                    cnt += 1
                else:
                    cnt -= 1
                if cnt == 0:
                    break
                j += 1
            if j == 1:
                return 1 + score(s[2:])
            else:
                return 2*score(s[1:j]) + score(s[j + 1:])
        return score(S)
