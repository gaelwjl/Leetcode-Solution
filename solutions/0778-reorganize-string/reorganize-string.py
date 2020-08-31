# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
#
# If possible, output any possible result.  If not possible, return the empty string.
#
# Example 1:
#
#
# Input: S = "aab"
# Output: "aba"
#
#
# Example 2:
#
#
# Input: S = "aaab"
# Output: ""
#
#
# Note:
#
#
# 	S will consist of lowercase letters and have length in range [1, 500].
#
#
#  
#


class Solution:
    def reorganizeString(self, S: str) -> str:
        c = Counter(S)
        chars_times = sorted(c.items(), key = lambda x: -x[1])
        if chars_times[0][1] > math.ceil(len(S) / 2):
            return ""
        ans = ['' for _ in range(len(S))]
        ind = 0
        for c, cnt in chars_times:
            while cnt:
                if ind >= len(ans): 
                    ind = 1
                ans[ind] = c
                ind += 2
                cnt -= 1

        return ''.join(ans)
