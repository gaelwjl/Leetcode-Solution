// Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
//
// You need to return the number of important reverse pairs in the given array.
//
// Example1:
//
// Input: [1,3,2,3,1]
// Output: 2
//
//
// Example2:
//
// Input: [2,4,3,5,1]
// Output: 3
//
//
// Note:
//
// The length of the given array will not exceed 50,000.
// All the numbers in the input array are in the range of 32-bit integer.
//
//


class Solution {
public:
    int reversePairs(vector<int>& nums) {
        int ans = 0, n = nums.size();
        function<void(int, int)> merge_sort = [&](int i, int j){
            if (i >= j) return ;
            int mid = (i + j) / 2;
            merge_sort(i, mid), merge_sort(mid + 1, j);
            // two pointers, k and l; 
            for (int k = i, l = mid + 1; k <= mid; k++){
                while (l <= j && nums[k] / 2.0 > nums[l])
                    l++;
                ans += (l - mid - 1);
            }
            sort(nums.begin() + i, nums.begin() + j + 1);
            return ;
        };
        merge_sort(0, n - 1);
        return ans;
    }
};

