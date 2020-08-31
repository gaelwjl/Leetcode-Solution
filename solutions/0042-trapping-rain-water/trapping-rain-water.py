# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
#
# Example:
#
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
#


class Solution:
    def trap(self, height):
        '''
        solutin using two pointers
        '''
        if len(height) == 0: return 0
        l, max_l = 0, height[0]
        r, max_r = len(height) - 1, height[len(height) - 1]
        ans = 0
        while l < r:
            if max_l < max_r:
                ans += max_l - height[l]
                l += 1
                max_l = max(max_l, height[l])
            else:
                ans += max_r - height[r]
                r -= 1
                max_r = max(max_r, height[r])
        return ans
        
