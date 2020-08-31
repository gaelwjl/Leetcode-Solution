// Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
//
// Example 1:
//
//
// Input:nums = [1,1,1], k = 2
// Output: 2
//
//
//  
// Constraints:
//
//
// 	The length of the array is in range [1, 20,000].
// 	The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
//
//


class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        vector<int> cum(nums.size() + 1, 0);
        for (int i = 0; i < nums.size(); i++)
            cum[i + 1] = cum[i] + nums[i];
        map<int, int> record;
        int ans = 0;
        for (int i=0;i<cum.size();i++){
            if (record.count(cum[i] - k))
                ans += record[cum[i] - k];
            record[cum[i]] += 1;
        }   
        return ans;
    }
};
