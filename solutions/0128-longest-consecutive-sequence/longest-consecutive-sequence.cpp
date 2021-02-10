// Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
//
//  
// Example 1:
//
//
// Input: nums = [100,4,200,1,3,2]
// Output: 4
// Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
//
//
// Example 2:
//
//
// Input: nums = [0,3,7,2,5,8,4,6,0,1]
// Output: 9
//
//
//  
// Constraints:
//
//
// 	0 <= nums.length <= 104
// 	-109 <= nums[i] <= 109
//
//
//  
// Follow up: Could you implement the O(n) solution?


class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int> m; 
        int r = 0; 
        for (auto i: nums){
            if (m[i]) 
                continue;
            r = max(r, m[i] = m[i + m[i + 1]] = m[i - m[i - 1]] = m[i - m[i - 1]] + m[i + m[i + 1]] + 1); 
        }
        return r;
    }
};
