# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
#
# Examples:
#
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode"
# return 2.
#
#
#  
#
# Note: You may assume the string contains only lowercase English letters.
#


class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)
        for i, ch in enumerate(s):
            if c[ch] == 1:
                return i
        return -1
