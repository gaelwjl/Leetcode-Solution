# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces  .
#
# Example 1:
#
#
# Input: "1 + 1"
# Output: 2
#
#
# Example 2:
#
#
# Input: " 2-1 + 2 "
# Output: 3
#
# Example 3:
#
#
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# Note:
#
#
# 	You may assume that the given expression is always valid.
# 	Do not use the eval built-in library function.
#
#


class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 0:
            return 0
        self.pos = 0
        def compute():
            ans, sgn = 0, 1
            tmp = 0
            while self.pos < len(s):
                n = s[self.pos]
                if n.isdigit():
                    tmp = tmp * 10 + int(n)
                    self.pos += 1
                elif n == "+" or n == '-':
                    ans += sgn * tmp
                    tmp = 0
                    sgn = 1 if (n == '+') else -1
                    self.pos += 1
                elif n == '(':
                    self.pos += 1
                    tmp = compute()
                elif n == ')':
                    self.pos += 1
                    ans += sgn*tmp
                    return ans
                else:
                    self.pos += 1
            ans += sgn*tmp
            return ans
        return compute()

