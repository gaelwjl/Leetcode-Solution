# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# If multiple answers are possible, just return any of them.
#
# Example 1:
#
#
# Input: numerator = 1, denominator = 2
# Output: "0.5"
#
#
# Example 2:
#
#
# Input: numerator = 2, denominator = 1
# Output: "2"
#
# Example 3:
#
#
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
#
#


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = []
        seen = {}
        x = numerator
        y = denominator
        if x == 0:
            return str(0)
        if x < 0 and y < 0:
            x = -x
            y = -y
        elif x < 0:
            x = -x
            res.append('-')
        elif y < 0:
            y = -y
            res.append('-')
        k, r = self.euclid(x, y)
        res.append(k)
        if r == 0:
            return "".join(map(str, res))
        res.append('.')
        while True:
            r *= 10
            k, r = self.euclid(r, y)
            res.append(k)
            if r in seen:
                break
            seen[r] = len(res) - 1
            if r == 0:
                return "".join(map(str, res))
        ind = seen[r] + 1
        return "".join(map(str, res[:ind])) + '(' + "".join(map(str, res[ind:])) + ')'
    
    def euclid(self, x, y):
        '''
        x >= 0, y > 0
        x = k * y + r
        return k, r
        '''
        k = x // y
        r = x - k * y
        return k, r
