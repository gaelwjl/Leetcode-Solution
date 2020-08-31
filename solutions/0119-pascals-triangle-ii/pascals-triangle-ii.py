# Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.
#
# Notice that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Follow up:
#
# Could you optimize your algorithm to use only O(k) extra space?
#
#  
# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
# Input: rowIndex = 0
# Output: [1]
# Example 3:
# Input: rowIndex = 1
# Output: [1,1]
#
#  
# Constraints:
#
#
# 	0 <= rowIndex <= 40
#
#


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            res = [1]
            previous = res
            for i in range(1, rowIndex + 1):
                res.append(1)
                for j in range(1, len(res) - 1):
                    res[j] = previous[j - 1] + previous[j]
                previous = res.copy()
            return res
