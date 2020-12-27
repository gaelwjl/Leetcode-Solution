// You are given an array nums consisting of non-negative integers. You are also given a queries array, where queries[i] = [xi, mi].
//
// The answer to the ith query is the maximum bitwise XOR value of xi and any element of nums that does not exceed mi. In other words, the answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements in nums are larger than mi, then the answer is -1.
//
// Return an integer array answer where answer.length == queries.length and answer[i] is the answer to the ith query.
//
//  
// Example 1:
//
//
// Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
// Output: [3,3,7]
// Explanation:
// 1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 1 XOR 3 = 2. The larger of the two is 3.
// 2) 1 XOR 2 = 3.
// 3) 5 XOR 2 = 7.
//
//
// Example 2:
//
//
// Input: nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
// Output: [15,-1,5]
//
//
//  
// Constraints:
//
//
// 	1 <= nums.length, queries.length <= 105
// 	queries[i].length == 2
// 	0 <= nums[j], xi, mi <= 109
//
//


class Solution {
public:
    struct Trie {
        vector<Trie*> nodes;
        Trie(): nodes(2) {}
        static void insert(Trie* root, int num){
            for (int i = 31; i >= 0; i--){
                int ind = (num >> i)&1;
                if (! (root -> nodes[ind]) )
                    root -> nodes[ind] = new Trie();
                root = root -> nodes[ind];
            }
        }
        
        static int query(Trie* root, int num){
            if (!root -> nodes[0] && !root -> nodes[1])
                return -1; 
            int ans = 0;
            for (int i = 31; i >= 0; i--){
                int ind = (num >> i) & 1;
                
                if (root -> nodes[1 - ind]){
                    root = root -> nodes[1 - ind]; 
                    ans |= (1 << i); 
                }else{
                    root = root -> nodes[ind];
                    // cout << i << endl; 
                    // assert(root != nullptr);
                }
            }
            return ans; 
        }
    };
    
    vector<int> maximizeXor(vector<int>& nums, vector<vector<int>>& queries) {
        int q = queries.size(); 
        vector<int> ans(q);
        vector<array<int, 3>> qry;
        sort(nums.begin(), nums.end()); 
        
        for (int i = 0; i < q; i++){
            qry.push_back({queries[i][1], queries[i][0], i}); 
        }
        sort(qry.begin(), qry.end());
        
        Trie* trie = new Trie();
        
        int j = 0; 
        for (int i = 0; i < q; i++){
            while (j < nums.size() && nums[j] <= qry[i][0]){
                trie -> insert(trie, nums[j]); 
                j++;
            }
            ans[qry[i][2]] = trie -> query(trie, qry[i][1]); 
        }
        return ans; 
    }
};
