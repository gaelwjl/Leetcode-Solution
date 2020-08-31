// You are given an m * n matrix, mat, and an integer k, which has its rows sorted in non-decreasing order.
//
// You are allowed to choose exactly 1 element from each row to form an array. Return the Kth smallest array sum among all possible arrays.
//
//  
// Example 1:
//
//
// Input: mat = [[1,3,11],[2,4,6]], k = 5
// Output: 7
// Explanation: Choosing one element from each row, the first k smallest sum are:
// [1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.  
//
// Example 2:
//
//
// Input: mat = [[1,3,11],[2,4,6]], k = 9
// Output: 17
//
//
// Example 3:
//
//
// Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
// Output: 9
// Explanation: Choosing one element from each row, the first k smallest sum are:
// [1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.  
//
//
// Example 4:
//
//
// Input: mat = [[1,1,10],[2,2,9]], k = 7
// Output: 12
//
//
//  
// Constraints:
//
//
// 	m == mat.length
// 	n == mat.length[i]
// 	1 <= m, n <= 40
// 	1 <= k <= min(200, n ^ m)
// 	1 <= mat[i][j] <= 5000
// 	mat[i] is a non decreasing array.
//
//


class Solution {
public:
    struct mycomp{
        bool operator ()(const pair<int, int> & lhs, const pair<int, int> & rhs)
        {
            return lhs.first + lhs.second < rhs.first + rhs.second;
        }
    };
    vector<int> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, mycomp> heap;
        int n = nums1.size(), m = nums2.size();
        for (int i = 0; i < min(k, n); i++){
            for (int j = 0; j < min(k, m); j++){
                if (heap.size() < k)
                    heap.push(make_pair(nums1[i], nums2[j]));
                else if (nums1[i] + nums2[j] < heap.top().first + heap.top().second){
                    heap.push(make_pair(nums1[i], nums2[j]));
                    heap.pop();
                }
            }
        }
        vector<int> res;
        while (!heap.empty()){
            int temp = 0;
            temp += (heap.top().first);
            temp += (heap.top().second);
            res.push_back(temp);
            heap.pop();
        }
        reverse(res.begin(), res.end());
        return res;
    }
    
    int kthSmallest(vector<vector<int>>& mat, int k) {
        int n = mat.size();
        int m = mat[0].size();
        vector<int> res = mat[0];
        for (int i = 1; i < n; i++){
            res = kSmallestPairs(res, mat[i], k);
        }
        return res[k - 1];
    }
};
