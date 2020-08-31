// Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
//
// Your algorithm's runtime complexity must be in the order of O(log n).
//
// If the target is not found in the array, return [-1, -1].
//
// Example 1:
//
//
// Input: nums = [5,7,7,8,8,10], target = 8
// Output: [3,4]
//
// Example 2:
//
//
// Input: nums = [5,7,7,8,8,10], target = 6
// Output: [-1,-1]
//
//  
// Constraints:
//
//
// 	0 <= nums.length <= 10^5
// 	-10^9 <= nums[i] <= 10^9
// 	nums is a non decreasing array.
// 	-10^9 <= target <= 10^9
//
//


class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        auto it = lower_bound(nums.begin(), nums.end(), target);
        if (nums.size() == 0 || it == nums.end() || *it != target) {
            vector<int> temp{-1, -1};
            return temp;
        }
        int begin = it - nums.begin();
        int end = begin;
        while (end < nums.size() && nums[end] == target){end++;}
        vector<int> temp{begin, --end};
        return temp;
        
    }
};
