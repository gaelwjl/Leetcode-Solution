# Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
#
# Example 1:
#
#
# Input: "2-1-1"
# Output: [0, 2]
# Explanation: 
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
#
# Example 2:
#
#
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation: 
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
#


class Solution:
    @lru_cache(None)
    def diffWaysToCompute(self, input: str) -> List[int]:
        res = []
        if input.isnumeric():
            return [int(input)]
        for i, c in enumerate(input):
            if c.isdigit():
                continue
            else:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                
                for l in left:
                    for r in right:
                        if c == '+':
                            res.append(l + r)
                        elif c == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        return res
