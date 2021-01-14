// Given an integer n, find a sequence that satisfies all of the following:
//
//
// 	The integer 1 occurs once in the sequence.
// 	Each integer between 2 and n occurs twice in the sequence.
// 	For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
//
//
// The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.
//
// Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution. 
//
// A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.
//
//  
// Example 1:
//
//
// Input: n = 3
// Output: [3,1,2,3,2]
// Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
//
//
// Example 2:
//
//
// Input: n = 5
// Output: [5,3,1,4,3,5,2,4,2]
//
//
//  
// Constraints:
//
//
// 	1 <= n <= 20
//
//


class Solution {
public:
    int n; 
    vector<int> used;
    bool dfs(vector<int>& cur, int i){
        if (i == 2*n - 1){
            return true;
        }
        if (cur[i] != -1)
            return dfs(cur, i + 1);
        for (int num = n; num >= 2; num--){
            if (!used[num] && i + num < 2*n - 1 && cur[i + num] == -1){
                cur[i] = num; 
                cur[i + num] = num; 
                used[num] = 1; 
                if (dfs(cur, i + 1)) 
                    return true; 
                used[num] = 0; 
                cur[i] = -1; 
                cur[i + num] = -1; 
            }
        }
        if (!used[1]){
            used[1] = 1; 
            cur[i] = 1; 
            if (dfs(cur, i + 1)) 
                return true; 
            used[1] = 0; 
            cur[i] = -1;
        }
        return false; 
    }
    
    vector<int> constructDistancedSequence(int n_) {
        if (n_ == 1) 
            return {1}; 
        n = n_; 
        vector<int> cur(2*n - 1, -1); 
        used = vector<int>(2*n - 1, 0);
        dfs(cur, 0); 
        return cur;
    }
};
