// Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.
//
// (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
//
// Return the number of good subarrays of A.
//
//  
//
// Example 1:
//
//
// Input: A = [1,2,1,2,3], K = 2
// Output: 7
// Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
//
//
// Example 2:
//
//
// Input: A = [1,2,1,3,4], K = 3
// Output: 3
// Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
//
//
//  
//
// Note:
//
//
// 	1 <= A.length <= 20000
// 	1 <= A[i] <= A.length
// 	1 <= K <= A.length
//


class Solution {
public:
    int subarraysWithKDistinct(vector<int>& A, int K) {
        int n = A.size(), window[20001], window_m[20001], j = 0, j_m = 0, ans = 0, diff = 0, diff_m = 0;
        memset(window, 0, sizeof(window)); 
        memset(window_m, 0, sizeof(window_m));
        for (int i = 0; i < n; i++) {
            if (window[A[i]] == 0){
                diff += 1; 
            }
            window[A[i]]++;
            while (diff > K){
                window[A[j]] --;
                if (window[A[j]] == 0)
                    diff--;
                j++;
            }
            
            if (window_m[A[i]] == 0)
                diff_m += 1;
            window_m[A[i]] ++;
            while (diff_m > K - 1){
                window_m[A[j_m]] --;
                if (window_m[A[j_m]] == 0) diff_m --;
                j_m ++;
            }
            if (diff == K) ans += j_m - j;
        }
        return ans;
    }
};

