// Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
//
// If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
//
// The replacement must be in place and use only constant extra memory.
//
//  
// Example 1:
// Input: nums = [1,2,3]
// Output: [1,3,2]
// Example 2:
// Input: nums = [3,2,1]
// Output: [1,2,3]
// Example 3:
// Input: nums = [1,1,5]
// Output: [1,5,1]
// Example 4:
// Input: nums = [1]
// Output: [1]
//
//  
// Constraints:
//
//
// 	1 <= nums.length <= 100
// 	0 <= nums[i] <= 100
//
//


class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        if (nums.size() <= 1) return ;
        int i = nums.size() - 2;
        for (; i >= 0 && nums[i] >= nums[i + 1]; i--);
        if (i < 0) {
            reverse(nums.begin(), nums.end());
            return ;
        }
        else {
            int j = nums.size() - 1;
            for (; j >= i; j--){
                if (nums[j] > nums[i]) break;
            }
            swap(nums[i], nums[j]);
            reverse(nums.begin() + i + 1, nums.end());
        }
        return ;
    }
};
