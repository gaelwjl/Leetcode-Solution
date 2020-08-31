// Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.
//
// If there is no non-empty subarray with sum at least K, return -1.
//
//  
//
//
//
//
//
// Example 1:
//
//
// Input: A = [1], K = 1
// Output: 1
//
//
//
// Example 2:
//
//
// Input: A = [1,2], K = 4
// Output: -1
//
//
//
// Example 3:
//
//
// Input: A = [2,-1,2], K = 3
// Output: 3
//
//
//  
//
// Note:
//
//
// 	1 <= A.length <= 50000
// 	-10 ^ 5 <= A[i] <= 10 ^ 5
// 	1 <= K <= 10 ^ 9
//
//
//
//
//


class Solution {
public:
    int shortestSubarray(vector<int>& A, int K) {
        deque<int> dq;
        vector<int> cumsum{0};
        for (int a: A)
            cumsum.push_back(a + cumsum.back());
        int ans = -1;
        for (int i = 0; i < cumsum.size(); i++){
            int p = cumsum[i];
            while (dq.size() && cumsum[dq.back()] >= p)
                dq.pop_back();
            
            dq.push_back(i);
            while (dq.size() && cumsum[dq.back()] - cumsum[dq.front()] >= K){
                if (ans == -1)
                    ans = dq.back() - dq.front();
                else
                    ans = min(ans, dq.back() - dq.front());
                dq.pop_front();
            }
        }
        return ans;
    }
};
