# Given a string s representing an expression, implement a basic calculator to evaluate it.
#
#  
# Example 1:
#
#
# Input: s = "1 + 1"
# Output: 2
#
#
# Example 2:
#
#
# Input: s = " 2-1 + 2 "
# Output: 3
#
#
# Example 3:
#
#
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 3 * 105
# 	s consists of digits, '+', '-', '(', ')', and ' '.
# 	s represents a valid expression.
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
