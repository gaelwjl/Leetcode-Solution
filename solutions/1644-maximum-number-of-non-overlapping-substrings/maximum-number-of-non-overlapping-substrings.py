# Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:
#
#
# 	The substrings do not overlap, that is for any two substrings s[i..j] and s[k..l], either j < k or i > l is true.
# 	A substring that contains a certain character c must also contain all occurrences of c.
#
#
# Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.
#
# Notice that you can return the substrings in any order.
#
#  
# Example 1:
#
#
# Input: s = "adefaddaccc"
# Output: ["e","f","ccc"]
# Explanation: The following are all the possible substrings that meet the conditions:
# [
#   "adefaddaccc"
#   "adefadda",
#   "ef",
#   "e",
#   "f",
#   "ccc",
# ]
# If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.
#
#
# Example 2:
#
#
# Input: s = "abbaccd"
# Output: ["d","bb","cc"]
# Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 10^5
# 	s contains only lowercase English letters.
#
#


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        tmp = {c:[s.index(c), s.rindex(c) + 1] for c in set(s)}
        # find all intervals: record l, r index of substrings
        inters = []
        for c in set(s):
            left, right = tmp[c]
            i, j = left, right
            while True:
                t = set(s[left:right])
                for c in t:
                    i = min(i, tmp[c][0])
                    j = max(j, tmp[c][1])
                if i == left and j == right:
                    break
                left = i
                right = j
            left = i
            right = j
            inters.append([left, right])

        inters = sorted(inters, key = lambda x: x[1])
        left = inters[0][0]
        right = inters[0][1]
        ans = [s[left:right]]
        
        for pair in inters:
            # how to know if there is any overlapping: 
            # or just greedily find the next one
            if pair[0] >= right or pair[1] <= left:
                ans.append(s[pair[0]:pair[1]])
                right = max(pair[1], right)
                left = min(pair[0], left)
        return ans
        
