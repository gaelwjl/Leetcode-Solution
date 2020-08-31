# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
#
# Note that after backspacing an empty text, the text will continue empty.
#
#
# Example 1:
#
#
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
#
#
#
# Example 2:
#
#
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
#
#
#
# Example 3:
#
#
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
#
#
#
# Example 4:
#
#
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
#
#
# Note:
#
#
# 	1 <= S.length <= 200
# 	1 <= T.length <= 200
# 	S and T only contain lowercase letters and '#' characters.
#
#
# Follow up:
#
#
# 	Can you solve it in O(N) time and O(1) space?
#
#
#
#
#
#


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_S = []
        for s in S:
            if s != '#':
                stack_S.append(s)
            elif stack_S:
                stack_S.pop(-1)
                
        stack_T = []
        for s in T:
            if s != '#':
                stack_T.append(s)
            elif stack_T:
                stack_T.pop(-1)
                
        print(stack_S)
        print(stack_T)
        
        if len(stack_S) != len(stack_T):
            return False
        for i in range(len(stack_S)):
            if stack_S[i] != stack_T[i]:
                return False
        return True
