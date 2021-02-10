// You are given a 2D integer array, queries. For each queries[i], where queries[i] = [ni, ki], find the number of different ways you can place positive integers into an array of size ni such that the product of the integers is ki. As the number of ways may be too large, the answer to the ith query is the number of ways modulo 109 + 7.
//
// Return an integer array answer where answer.length == queries.length, and answer[i] is the answer to the ith query.
//
//  
// Example 1:
//
//
// Input: queries = [[2,6],[5,1],[73,660]]
// Output: [4,1,50734910]
// Explanation: Each query is independent.
// [2,6]: There are 4 ways to fill an array of size 2 that multiply to 6: [1,6], [2,3], [3,2], [6,1].
// [5,1]: There is 1 way to fill an array of size 5 that multiply to 1: [1,1,1,1,1].
// [73,660]: There are 1050734917 ways to fill an array of size 73 that multiply to 660. 1050734917 modulo 109 + 7 = 50734910.
//
//
// Example 2:
//
//
// Input: queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]
// Output: [1,2,3,10,5]
//
//
//  
// Constraints:
//
//
// 	1 <= queries.length <= 104 
// 	1 <= ni, ki <= 104
//
//


class Solution {
public:
    int get_factors(int& i, int p){
        int f = 0;
        while (i % p == 0){
            f ++; 
            i /= p;
        }
        return f;
    }
    vector<int> waysToFillArray(vector<vector<int>>& queries) {
        vector<int> res;
        vector<vector<int>> comb(10020, vector<int>(30, 1));
        int mod = 1e9 + 7;
        int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
                53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
        
        for (int i = 1; i < 10020; i++){
            // cout << comb[i][0] << endl;
            for (int j = 1; j < min(i, 30); j++){
                comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1])%mod;
            }
        }
        for (auto q: queries){
            int n = q[0], k = q[1], ways = 1;
            
            for (auto p: primes){
                int f = get_factors(k, p);
                ways = (long) ways * comb[f + n - 1][f] % mod;
            }
            if (k != 1)
                ways = (long) ways * n % mod;
            res.push_back(ways);
        }
        return res;
    }
};
