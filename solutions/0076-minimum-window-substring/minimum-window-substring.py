# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#
# Example:
#
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
#
#
# Note:
#
#
# 	If there is no such window in S that covers all characters in T, return the empty string "".
# 	If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
#
#


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter, defaultdict
        tc = Counter(t)
        
        required = 0
        for k, v in tc.items():
            if v > 0:
                required += 1
        ans = [float('inf'), 0, len(s)]
        window = defaultdict(int)
        l, r = 0, 0
        formed = 0
        while r < len(s):
            window[s[r]] += 1
            if window[s[r]] == tc[s[r]] and tc[s[r]]:
                formed += 1
            # it should be an equality, otherwise won't work
            while l <= r and formed == required:
                if r - l + 1 < ans[0]:
                    ans = [r - l + 1, l, r]
                window[s[l]] -= 1
                if window[s[l]] < tc[s[l]]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]
