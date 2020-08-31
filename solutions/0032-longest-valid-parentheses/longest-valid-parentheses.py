# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
# Example 1:
#
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
#
#
# Example 2:
#
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
#
#


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxlen = 0
        for i in range(len(s)):
            if s[i] == ')':
                if stack[-1] != -1 and s[stack[-1]] == '(':
                    last = stack.pop(-1)
                    maxlen = max(maxlen, i - stack[-1])
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return maxlen
