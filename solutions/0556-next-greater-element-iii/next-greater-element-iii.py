# Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.
#
# Example 1:
#
#
# Input: 12
# Output: 21
#
#
#  
#
# Example 2:
#
#
# Input: 21
# Output: -1
#
#
#  
#


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(map(int, str(n)))
        i = len(s) - 1
        while i >= 1 and s[i] <= s[i - 1]:
            i -= 1
        if i == 0:
            return -1
        j = i
        i -= 1
        while j < len(s) and s[j] > s[i]:
            j += 1
        j -= 1
        s[i], s[j] = s[j], s[i]
        s[i + 1:] = s[i + 1:][::-1]
        ans = int("".join(map(str, s)))
        return ans if ans <= ((1 << 31) - 1) else -1
