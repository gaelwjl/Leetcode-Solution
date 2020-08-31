# Given two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Return the median of the two sorted arrays.
#
# Follow up: The overall run time complexity should be O(log (m+n)).
#
#  
# Example 1:
#
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
#
# Example 2:
#
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
# Example 3:
#
#
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
#
#
# Example 4:
#
#
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
#
#
# Example 5:
#
#
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
#
#
#  
# Constraints:
#
#
# 	nums1,length == m
# 	nums2,length == n
# 	0 <= m <= 1000
# 	0 <= n <= 1000
# 	1 <= m + n <= 2000
#
#


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (len(nums1) > len(nums2)):
            temp = nums1
            nums1 = nums2
            nums2 = temp
        x = len(nums1)
        y = len(nums2)
        TotLen = x + y
        if (x == 0):
            if (TotLen%2==0):
                return (nums2[math.floor(y/2)-1] + nums2[math.floor(y/2)])/2
            else:
                return (nums2[math.floor(y/2)])
        if (x == 1 and y == 1):
            return (nums1[0]+nums2[0])/2
        if (x == 1):
            if (nums1[0] < nums2[math.floor((TotLen+1)/2) - 1]):
                if (TotLen % 2 == 0):
                    median = (max(nums1[0], nums2[math.floor((TotLen+1)/2) - 2]) + nums2[math.floor((TotLen+1)/2) - 1])/2
                    return median
                else: 
                    return max(nums1[0], nums2[math.floor((TotLen+1)/2) - 2])
            else:
                if (TotLen % 2 == 0):
                    median = (nums2[math.floor((TotLen+1)/2)-1] + min(nums1[0], nums2[math.floor((TotLen+1)/2)]))/2
                    return median
                else: 
                    return nums2[math.floor((TotLen+1)/2) - 1]

        ParX = math.floor(x/2) #numbers of elements on the left in nums1
        ParY = math.floor((TotLen + 1) / 2) - ParX

        while (ParX < x and ParX > 0 and ParY  > 0 and ParY < y):
            if (nums1[ParX-1] > nums2[ParY]):
                ParX = ParX - 1
                ParY = ParY + 1
                continue
            if (nums1[ParX] < nums2[ParY - 1]):
                ParX = ParX + 1
                ParY = ParY - 1
                continue
            else:
                break
        if (ParX == x and ParY != 0):
            LMax = max(nums1[ParX-1], nums2[ParY - 1])
            RMax = nums2[ParY]
        elif(ParX != 0 and ParY == y):
            LMax = max(nums1[ParX-1], nums2[ParY - 1])
            RMax = nums1[ParX]
        elif(ParX == 0 and ParY < y):
            LMax = nums2[math.floor((TotLen+1)/2)-1]
            RMax = min(nums1[0], nums2[math.floor((TotLen+1)/2)])
        elif(ParX == 0 and ParY == y):
            LMax = nums2[y - 1]
            RMax = nums1[0]
        elif(ParY == 0): #in this case ParX == x 
            LMax = nums1[ParX-1]
            RMax = nums2[0]
        else:
            LMax = max(nums1[ParX-1], nums2[ParY - 1])
            RMax = min(nums1[ParX], nums2[ParY])

        if (TotLen % 2 == 0):
            median = (LMax + RMax) / 2
            return median
        else:
            return LMax


