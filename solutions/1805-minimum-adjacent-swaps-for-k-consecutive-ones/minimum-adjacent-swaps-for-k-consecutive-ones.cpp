// You are given an integer array, nums, and an integer k. nums comprises of only 0's and 1's. In one move, you can choose two adjacent indices and swap their values.
//
// Return the minimum number of moves required so that nums has k consecutive 1's.
//
//  
// Example 1:
//
//
// Input: nums = [1,0,0,1,0,1], k = 2
// Output: 1
// Explanation: In 1 move, nums could be [1,0,0,0,1,1] and have 2 consecutive 1's.
//
//
// Example 2:
//
//
// Input: nums = [1,0,0,0,0,0,1,1], k = 3
// Output: 5
// Explanation: In 5 moves, the leftmost 1 can be shifted right until nums = [0,0,0,0,0,1,1,1].
//
//
// Example 3:
//
//
// Input: nums = [1,1,0,1], k = 2
// Output: 0
// Explanation: nums already has 2 consecutive 1's.
//
//
//  
// Constraints:
//
//
// 	1 <= nums.length <= 105
// 	nums[i] is 0 or 1.
// 	1 <= k <= sum(nums)
//
//


class Solution {
public:
    int minMoves(vector<int>& nums, int k) {
        int n = nums.size(); 
        vector<int> pos; 
        for (int i = 0; i < n; i++){
            if (nums[i]){
                pos.push_back(i - pos.size()); 
            }
        }
        int l = (k + 1) / 2; int r = k - l;
        
        int leftc = 0, rightc = 0; // left sum and right sum;
        
        for (int i = 0; i < k; i++){
            if (i <= l - 1){
                leftc += pos[i];
            }else{
                rightc += pos[i];
            }
        }
        // formula to compute cost from left sum and right sum 
        int minc = rightc - leftc + pos[k / 2]*(l - r);
        
        for (int i = 0; i + k < pos.size(); i++){
            // window from i + 1 to i + k inclusive
            int med = i + (k + 1)/2;
            leftc += pos[med] - pos[i];
            rightc += pos[i + k] - pos[med];
            minc = min(minc, rightc - leftc + pos[med]*(l - r));
        }
        return minc; 
    }
};
