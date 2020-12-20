// Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
//
// Follow up: The overall run time complexity should be O(log (m+n)).
//
//  
// Example 1:
//
//
// Input: nums1 = [1,3], nums2 = [2]
// Output: 2.00000
// Explanation: merged array = [1,2,3] and median is 2.
//
//
// Example 2:
//
//
// Input: nums1 = [1,2], nums2 = [3,4]
// Output: 2.50000
// Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
//
//
// Example 3:
//
//
// Input: nums1 = [0,0], nums2 = [0,0]
// Output: 0.00000
//
//
// Example 4:
//
//
// Input: nums1 = [], nums2 = [1]
// Output: 1.00000
//
//
// Example 5:
//
//
// Input: nums1 = [2], nums2 = []
// Output: 2.00000
//
//
//  
// Constraints:
//
//
// 	nums1.length == m
// 	nums2.length == n
// 	0 <= m <= 1000
// 	0 <= n <= 1000
// 	1 <= m + n <= 2000
// 	-106 <= nums1[i], nums2[i] <= 106
//
//


class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size() + nums2.size();
        if (n == 1) {
            if (nums1.size()) return nums1[0];
            else return nums2[0];
        }
        vector<int> seen;
        int i = 0, j = 0;
        for (int c = 0; c < ceil((n+1)/2.0); c++){
            // cout << i << " " << j << endl;
            if (j >= nums2.size() || (i < nums1.size()&&nums1[i] <= nums2[j])){
                seen.push_back(nums1[i]);
                i++;
            }
            else{
                seen.push_back(nums2[j]);
                j++;
            }
        }
        if (n&1){
            return seen.back();
        }
        else{
            return ((double) seen.back() + (double) seen[seen.size() - 2]) / 2.0;
        }
    }
};
