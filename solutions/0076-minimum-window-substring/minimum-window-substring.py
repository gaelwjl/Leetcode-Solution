# Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".
#
# Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.
#
#  
# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
#
#  
# Constraints:
#
#
# 	1 <= s.length, t.length <= 105
# 	s and t consist of English letters.
#
#
#  
# Follow up: Could you find an algorithm that runs in O(n) time?


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        if len(t) == 0:
            return ""
        i, j = 0, 0
        ct = Counter(t)
        tmp = defaultdict(int)
        c, required = 0, len(ct.keys())
        ans, res_s = float('inf'), ""
        while j < n:
            while j < n and c < required:
                tmp[s[j]] += 1
                if ct[s[j]] > 0 and tmp[s[j]] == ct[s[j]]:
                    c += 1
                j += 1
            # continue to advance i if s[i] not in t
            while i < n:
                if tmp[s[i]] > ct[s[i]]:
                    tmp[s[i]] -= 1
                    i += 1
                    
                else:
                    break
            # print(s[i:j])
            if c == required: 
                if j - i < ans: 
                    res_s = s[i:j]
                    ans = j - i
                while c == required:
                    tmp[s[i]] -= 1
                    if ct[s[i]] > 0 and tmp[s[i]] < ct[s[i]]:
                        
                        c -= 1
                    i += 1
            # continue to advance i if s[i] not in t
            while i < n:
                if tmp[s[i]] > ct[s[i]]:
                    tmp[s[i]] -= 1
                    i += 1
                else:
                    break
        return res_s
                
                
