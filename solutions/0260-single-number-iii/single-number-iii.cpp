// Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
//
// Follow up: Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
//
//  
// Example 1:
//
//
// Input: nums = [1,2,1,3,2,5]
// Output: [3,5]
// Explanation:  [5, 3] is also a valid answer.
//
//
// Example 2:
//
//
// Input: nums = [-1,0]
// Output: [-1,0]
//
//
// Example 3:
//
//
// Input: nums = [0,1]
// Output: [1,0]
//
//
//  
// Constraints:
//
//
// 	1 <= nums.length <= 30000
// 	 Each integer in nums will appear twice, only two integers will appear once.
//
//


class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int all = 0; 
        for (int e: nums){
            all ^= e; 
        }
        int i = 0; 
        while ((all & 1) == 0){ 
            all >>= 1; 
            i += 1; 
        }
        vector<int> ans(2, 0);
        for (int it = 0; it < nums.size(); it++){
            if (nums[it] & (1 << i))
                ans[0] ^= nums[it]; 
            else ans[1] ^= nums[it];
        }
        return ans;
    }
};
