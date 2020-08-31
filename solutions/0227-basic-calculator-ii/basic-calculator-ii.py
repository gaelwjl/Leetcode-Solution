# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces  . The integer division should truncate toward zero.
#
# Example 1:
#
#
# Input: "3+2*2"
# Output: 7
#
#
# Example 2:
#
#
# Input: " 3/2 "
# Output: 1
#
# Example 3:
#
#
# Input: " 3+5 / 2 "
# Output: 5
#
#
# Note:
#
#
# 	You may assume that the given expression is always valid.
# 	Do not use the eval built-in library function.
#
#


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sgn, op = 1, 0
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            elif s[i].isdigit():
                j = i + 1
                n = s[i]
                while j < len(s) and s[j].isdigit():
                    n += s[j]
                    j += 1
                i = j
                n = int(n)
                if op == 0: 
                    stack.append(sgn*n)
                elif op == 1:
                    n1 = stack.pop()
                    stack.append(n1 * n)
                elif op == -1:
                    n1 = stack.pop()
                    stack.append(int(n1 / n))
            elif s[i] == '*':
                op = 1
                i += 1
            elif s[i] == '/':
                op = -1
                i += 1
            elif s[i] == '+':
                op = 0
                sgn = 1 
                i += 1
            elif s[i] == '-':
                op = 0
                sgn = -1
                i += 1
        return int(sum(stack))
