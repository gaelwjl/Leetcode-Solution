# A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.
#
# Given three integers a, b and c, return any string s, which satisfies following conditions:
#
#
# 	s is happy and longest possible.
# 	s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
# 	s will only contain 'a', 'b' and 'c' letters.
#
#
# If there is no such string s return the empty string "".
#
#  
# Example 1:
#
#
# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
#
#
# Example 2:
#
#
# Input: a = 2, b = 2, c = 1
# Output: "aabbc"
#
#
# Example 3:
#
#
# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It's the only correct answer in this case.
#
#
#  
# Constraints:
#
#
# 	0 <= a, b, c <= 100
# 	a + b + c > 0
#
#


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        chars = "abc"
        f = [a, b, c]
        added = [0, 0, 0]
        n = a + b + c
        for _ in range(n):
            for i in range(3):
                if f[i] > 0:
                    j = (i + 1) % 3
                    k = (i + 2) % 3
                    if (f[i] >= f[j] and f[i] >= f[k] and added[i] != 2) or (added[j] == 2 or added[k] == 2):
                        f[i] -= 1
                        res.append(chars[i])
                        added[i] += 1
                        added[j] = 0
                        added[k] = 0
            
        return ''.join(res)
