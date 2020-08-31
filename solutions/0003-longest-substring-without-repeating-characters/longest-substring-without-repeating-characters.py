# Given a string, find the length of the longest substring without repeating characters.
#
#
# Example 1:
#
#
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
#
#
#
# Example 2:
#
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
#
# Example 3:
#
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
#
#
#
#


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mymap = {}
        i = 0
        n = len(s)
        max_ = 0
        for j in range(n):
            if s[j] in mymap:
                i = max(i, mymap[s[j]])
            max_ = max(max_, j - i + 1)
            mymap[s[j]] = j + 1
        return max_
            
