# Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
#
# You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.
#
#  
# Example 1:
#
#
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
#
#
# Example 2:
#
#
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
#
#
# Example 3:
#
#
# Input: name = "leelee", typed = "lleeelee"
# Output: true
#
#
# Example 4:
#
#
# Input: name = "laiden", typed = "laiden"
# Output: true
# Explanation: It's not necessary to long press any character.
#
#
#  
# Constraints:
#
#
# 	1 <= name.length <= 1000
# 	1 <= typed.length <= 1000
# 	The characters of name and typed are lowercase letters.
#
#


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i_n = 0
        j_t = 0
        while i_n < len(name):
            #get numbers of name[i_n] in the string name
            l_n = 1
            while i_n + l_n < len(name) and name[i_n + l_n] == name[i_n]:
                l_n += 1
            
            l_t = 0
            while j_t + l_t < len(typed) and typed[j_t + l_t] == name[i_n]:
                l_t += 1
        
            if l_t < l_n or l_t == 0:
                return False
            i_n = i_n + l_n
            j_t = l_t + j_t
        return True
