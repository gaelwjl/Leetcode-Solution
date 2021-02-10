// You are given an integer array nums and an integer goal.
//
// You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. That is, if the sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).
//
// Return the minimum possible value of abs(sum - goal).
//
// Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original array.
//
//  
// Example 1:
//
//
// Input: nums = [5,-7,3,5], goal = 6
// Output: 0
// Explanation: Choose the whole array as a subsequence, with a sum of 6.
// This is equal to the goal, so the absolute difference is 0.
//
//
// Example 2:
//
//
// Input: nums = [7,-9,15,-2], goal = -5
// Output: 1
// Explanation: Choose the subsequence [7,-9,-2], with a sum of -4.
// The absolute difference is abs(-4 - (-5)) = abs(1) = 1, which is the minimum.
//
//
// Example 3:
//
//
// Input: nums = [1,2,3], goal = -7
// Output: 7
//
//
//  
// Constraints:
//
//
// 	1 <= nums.length <= 40
// 	-107 <= nums[i] <= 107
// 	-109 <= goal <= 109
//
//


class Solution {
public:
    int minAbsDifference(vector<int>& nums, int goal) {
        set<int> part1{0}, part2{0};
        int n = nums.size(), ans = abs(goal);
        for (int i = 0; i < n / 2; i++) {
            for (auto& v: vector<int>(part1.begin(), part1.end())){
                part1.insert(v + nums[i]); 
            }
        }
        auto it = part1.lower_bound(goal); 
        if (it != part1.end()) ans = min(ans, abs(goal - *it)); 
        if (it != part1.begin()) ans = min(ans, abs(goal - *prev(it)));
        for (int i = n / 2; i < n; i++) {
            for (auto& v: vector<int>(part2.begin(), part2.end())){
                if (part2.insert(v + nums[i]).second)
                {
                    // two sum
                    auto it = part1.lower_bound(goal - v - nums[i]);
                    if (it != part1.end())
                        ans = min(ans, abs(goal - nums[i] - v - *it));
                    if (it != part1.begin())
                        ans = min(ans, abs(goal - nums[i] - v - *prev(it)));
                    if (ans == 0)
                        return 0;
                }
            }
        }
        return ans; 
    }
};

