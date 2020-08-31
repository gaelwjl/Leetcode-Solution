// You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
//
// Define a pair (u,v) which consists of one element from the first array and one element from the second array.
//
// Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
//
// Example 1:
//
//
// Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
// Output: [[1,2],[1,4],[1,6]] 
// Explanation: The first 3 pairs are returned from the sequence: 
//              [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
//
// Example 2:
//
//
// Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
// Output: [1,1],[1,1]
// Explanation: The first 2 pairs are returned from the sequence: 
//              [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
//
// Example 3:
//
//
// Input: nums1 = [1,2], nums2 = [3], k = 3
// Output: [1,3],[2,3]
// Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
//
//


class Solution {
    struct mycomp{
        bool operator ()(const pair<int, int> & lhs, const pair<int, int> & rhs)
        {
            return lhs.first + lhs.second < rhs.first + rhs.second;
        }
    };
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
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
        vector<vector<int>> res;
        while (!heap.empty()){
            vector<int> temp;
            temp.push_back(heap.top().first);
            temp.push_back(heap.top().second);
            res.push_back(temp);
            heap.pop();
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
