#
# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.
#
#
# Example 1:
#
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
#
#
#
# Example 2:
#
# Input: 9973
# Output: 9973
# Explanation: No swap.
#
#
#
#
# Note:
#
# The given number is in the range [0, 108]
#
#


class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(map(int, str(num)))
        last_seen = {x:i for i, x in enumerate(num)}
        for i in range(len(num)):
            for d in range(9, num[i], -1):
                if d in last_seen and last_seen[d] > i:
                    num[i], num[last_seen[d]] = num[last_seen[d]], num[i]
                    return int("".join(map(str, num)))
        return int("".join(map(str,num)))
    
        

