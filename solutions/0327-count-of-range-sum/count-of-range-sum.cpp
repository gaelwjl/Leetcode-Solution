// Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
// Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.
//
// Note:
// A naive algorithm of O(n2) is trivial. You MUST do better than that.
//
// Example:
//
//
// Input: nums = [-2,5,-1], lower = -2, upper = 2,
// Output: 3 
// Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
//
//  
// Constraints:
//
//
// 	0 <= nums.length <= 10^4
//
//


class Solution {
public:
    int countRangeSum(vector<int>& arr, int lower, int upper) {
        // solution by divide and conquer
        int n = arr.size(), ans = 0;
        vector<long long> nums(n + 1);
        for (int i = 1; i <= n; i++) 
            nums[i] = nums[i - 1] + arr[i - 1];
        function<void(int, int)> merge_sort = [&](int lo, int hi){
            if (lo + 1 >= hi) {
                return ;
            }
            int mid = (lo + hi) / 2;
            int i = mid, j = mid, cnt = 0;
            merge_sort(lo, mid), merge_sort(mid, hi);
            
            for (int left = lo; left < mid; ++left){
                int vl = nums[left];
                while (i < hi && nums[i] - vl < lower) i++;
                while (j < hi && nums[j] - vl <= upper) j++;
                ans += j - i;
            }
            sort(nums.begin() + lo, nums.begin() + hi);
            return ;
        };
        merge_sort(0, n + 1);
        return ans;
    }
};

