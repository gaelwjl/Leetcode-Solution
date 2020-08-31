# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
#
# Follow up:
# Could you solve it in linear time?
#
# Example:
#
#
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7] 
# Explanation: 
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 10^5
# 	-10^4 <= nums[i] <= 10^4
# 	1 <= k <= nums.length
#
#


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = deque()
        j = 0
        ans = []
        for i in range(len(nums)):
            while pq and nums[i] > nums[pq[-1]]:
                pq.pop()
            pq.append(i)
            while pq and i - pq[0] + 1 > k:
                pq.popleft()
            if i >= k - 1:
                ans.append(nums[pq[0]])
        return ans            
