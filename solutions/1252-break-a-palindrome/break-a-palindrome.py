# Given a palindromic string palindrome, replace exactly one character by any lowercase English letter so that the string becomes the lexicographically smallest possible string that isn't a palindrome.
#
# After doing so, return the final string.  If there is no way to do so, return the empty string.
#
#  
# Example 1:
#
#
# Input: palindrome = "abccba"
# Output: "aaccba"
#
#
# Example 2:
#
#
# Input: palindrome = "a"
# Output: ""
#
#
#  
# Constraints:
#
#
# 	1 <= palindrome.length <= 1000
# 	palindrome consists of only lowercase English letters.
#


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        r = len(palindrome)
        lowers = "abcdefghijklmnopqrstuvwxyz"
        for l in range(0, r // 2):
            if ord(palindrome[l]) - ord('a'):
                return palindrome[0:l] + 'a' + palindrome[l + 1:]
        return palindrome[0:r - 1] + 'b'
                
            
