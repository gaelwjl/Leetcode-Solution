// Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B. 
//
// Example 1:
//
// Input:
// nums = [1,3,1]
// k = 1
// Output: 0 
// Explanation:
// Here are all the pairs:
// (1,3) -> 2
// (1,1) -> 0
// (3,1) -> 2
// Then the 1st smallest distance pair is (1,1), and its distance is 0.
//
//
//
// Note:
//
// 2 <= len(nums) <= 10000.
// 0 <= nums[i] < 1000000.
// 1 <= k <= len(nums) * (len(nums) - 1) / 2.
//
//


class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int l = 0, r = nums.back() - nums.front();
        while (l <= r){
            int mid = (l + r) / 2;
            int count = 0;
            int j = 0;
            for (int i = 0; i < nums.size(); i++){
                while (j < nums.size() && nums[j] - nums[i] <= mid){
                    j++;
                }
                count += (j - i - 1);
            }
            // cout << mid << " " << count << endl;
            if (count >= k){
                r = mid - 1;
            }
            else{
                l = mid + 1;
            }
        }
        return l;
    }
};
