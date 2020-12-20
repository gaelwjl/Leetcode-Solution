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
        self.i = 0
        def recurse(s):
            stk = []
            cum, op = 0, 1
            while self.i < len(s):
                if s[self.i] == ' ':
                    self.i += 1
                    continue 
                if s[self.i].isdigit():
                    cum = cum * 10 + ord(s[self.i]) - ord('0')
                    self.i += 1
                elif s[self.i] == '+':
                    stk.append(cum*op)
                    cum = 0
                    op = 1
                    self.i += 1
                elif s[self.i] == '-':
                    stk.append(cum*op)
                    cum = 0
                    op = -1
                    self.i += 1
                elif s[self.i] == '(':
                    self.i += 1
                    stk.append(op*recurse(s))
                    op = 1
                elif s[self.i] == ')':
                    self.i += 1
                    stk.append(cum*op)
                    return sum(stk)
                
            if cum: 
                stk.append(cum*op)
            # print(stk)
            return sum(stk)
        
        return recurse(s)
