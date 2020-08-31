# Given an integer array of digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order.
#
# Since the answer may not fit in an integer data type, return the answer as a string.
#
# If there is no answer return an empty string.
#
#  
# Example 1:
#
#
# Input: digits = [8,1,9]
# Output: "981"
#
#
# Example 2:
#
#
# Input: digits = [8,6,7,1,0]
# Output: "8760"
#
#
# Example 3:
#
#
# Input: digits = [1]
# Output: ""
#
#
# Example 4:
#
#
# Input: digits = [0,0,0,0,0,0]
# Output: "0"
#
#
#  
# Constraints:
#
#
# 	1 <= digits.length <= 10^4
# 	0 <= digits[i] <= 9
# 	The returning answer must not contain unnecessary leading zeros.
#
#


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        c = Counter(digits)
        def get_ans(exc):
            for d in exc:
                c[d] -= 1
            ans = []
            for d in range(9, 0, -1):
                ans += [d]*c[d]
            if ans:
                ans += [0] * c[0]
            else:
                ans += [0]*min(1, c[0])
            return ans
        sd = sum(digits)
        todiv = [[0, 3, 6, 9], [1, 4, 7], [2, 5, 8]]
        r = sd % 3
        if r == 0:
            return "".join(map(str, get_ans([])))
        for d in todiv[r]:
            if c[d]:
                return "".join(map(str, get_ans([d])))
        for d1, d2 in zip(todiv[3 - r], todiv[3 - r]):
            if d1 == d2 and c[d1] >= 2 or d1 != d2 and c[d1] >= 1 and c[d2] >= 1:
                return "".join(map(str, get_ans([d1, d2])))
        return ""
