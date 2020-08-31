# Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits.
#
# Note: You should try to optimize your time and space complexity.
#
# Example 1:
#
#
# Input:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# Output:
# [9, 8, 6, 5, 3]
#
# Example 2:
#
#
# Input:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# Output:
# [6, 7, 6, 0, 4]
#
# Example 3:
#
#
# Input:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# Output:
# [9, 8, 9]
#


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def maxi(nums, k):
            if k == 0:
                return []
            res = []
            topop = len(nums) - k
            for i in range(len(nums)):
                while res and res[-1] < nums[i] and topop:
                    res.pop(-1)
                    topop -= 1
                res.append(nums[i])
            return res[:k]
                
        def merge(a, b):
            return [max(a, b).pop(0) for _ in a + b]
        
        return max([merge(maxi(nums1, i), maxi(nums2, k - i)) for i in range(k + 1) 
                    if i <= len(nums1) and k - i <= len(nums2)
                   ])
            
