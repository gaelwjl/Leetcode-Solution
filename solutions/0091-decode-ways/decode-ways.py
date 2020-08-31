# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# Example 1:
#
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
#
# Example 2:
#
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
#


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0
        if "00" in s:
            return 0
        dp_y = [0] * n
        dp_n = [0] * n
        dp_n[0] = 1
        if 1 <= int(s[0:2]) <= 26 and n >= 2:
            dp_y[1] = 1
        for i in range(1, n):
            if i >= 2 and 1 <= int(s[i - 1:i + 1]) <= 26 and s[i - 1] != '0':
                dp_y[i] = dp_n[i - 2] + dp_y[i - 2]
            if int(s[i]) != 0:
                dp_n[i] = dp_n[i - 1] + dp_y[i - 1]
            else:
                dp_n[i] = 0
        print(dp_y)
        return dp_y[n - 1] + dp_n[n - 1]
