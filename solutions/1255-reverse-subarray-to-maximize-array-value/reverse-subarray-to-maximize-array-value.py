# You are given an integer array nums. The value of this array is defined as the sum of |nums[i]-nums[i+1]| for all 0 <= i < nums.length-1.
#
# You are allowed to select any subarray of the given array and reverse it. You can perform this operation only once.
#
# Find maximum possible value of the final array.
#
#  
# Example 1:
#
#
# Input: nums = [2,3,1,5,4]
# Output: 10
# Explanation: By reversing the subarray [3,1,5] the array becomes [2,5,1,3,4] whose value is 10.
#
#
# Example 2:
#
#
# Input: nums = [2,4,9,24,2,1,10]
# Output: 68
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 3*10^4
# 	-10^5 <= nums[i] <= 10^5
#


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        if n==2:
            return abs(nums[0]-nums[1])
        orig=sum([abs(nums[i]-nums[i+1]) for i in range(n-1)])
        M1=max([abs(nums[i]-nums[-1])-abs(nums[i]-nums[i+1]) for i in range(n-2)])
        M2=max([abs(nums[i]-nums[0])-abs(nums[i]-nums[i-1]) for i in range(2,n)])
        L=[sorted([nums[i],nums[i+1]]) for i in range(n-1)]
        m=min([x[1] for x in L])
        M=max([x[0] for x in L])
        if M<=m:
            M3=0
        else:
            M3=2*(M-m)
        return orig+max(M1,M2,M3)
                    
