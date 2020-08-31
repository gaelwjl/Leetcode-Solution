# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
#
#
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
#


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_list, cur = [0]*26, [0]*26
        ans = []
        if len(p) > len(s):
            return []
        for i in range(len(p)):
            p_list[ord(p[i]) - ord('a')] += 1
            cur[ord(s[i]) - ord('a')] += 1
        for i in range(len(p), len(s)):
            if cur == p_list:
                ans.append(i - len(p))
            cur[ord(s[i - len(p) ]) - ord('a') ] -= 1
            cur[ord(s[i]) - ord('a')] += 1
        if cur == p_list:
                ans.append(len(s) - len(p))
        return ans
