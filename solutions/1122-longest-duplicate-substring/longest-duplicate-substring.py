# Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)
#
# Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)
#
#  
#
# Example 1:
#
#
# Input: "banana"
# Output: "ana"
#
#
# Example 2:
#
#
# Input: "abcd"
# Output: ""
#
#
#  
#
# Note:
#
#
# 	2 <= S.length <= 10^5
# 	S consists of lowercase English letters.
#
#


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        mod = 2**63 - 1
        s = [ord(c) - ord('a') for c in S]
        def test(length):
            #suppose there is no collision
            p = pow(26, length, mod)
            cur = reduce(lambda x, y : (x*26 + y) % mod, s[:length], 0)
            seen = {cur}
            for i in range(length, len(s)):
                cur = (cur * 26 + s[i] - s[i - length] * p) % mod
                if cur in seen:
                    return i - length + 1
                seen.add(cur)
        lo = 0
        hi = len(s) - 1
        ans = ""
        while lo < hi:
            mid = (lo + hi + 1) // 2
            pos = test(mid)
            if pos != None:
                lo = mid
                ans = S[pos: pos + mid]
            else:
                hi = mid - 1
        return ans
