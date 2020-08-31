# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: "cbbd"
# Output: "bb"
#
#


class Solution:
    def longestPalindrome(self, s: str) -> str:
        assert('$' not in s and '^' not in s and '#' not in s)
        if s == '':
            return ''
        t = '^#' + "#".join(s) + "#$"
        c = 0
        d = 0
        #les rayons du palindrom cnetre en j
        P = [0 for _ in range(len(t))]
        for  i in range(1, len(t) - 1):
            mirroir = 2 * c - i
            P[i] = max(0, min(d - i, P[mirroir]))
            
            while t[i + 1 + P[i]] == t[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > d:
                c = i
                d = i + P[i]
        (k, i) = max((P[i], i) for i in range(1, len(t) - 1))
        (start, end) = ((i - k) // 2, (i + k) // 2)
        return s[start:end]
                    
