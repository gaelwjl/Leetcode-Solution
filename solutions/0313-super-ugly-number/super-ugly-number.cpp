// Write a program to find the nth super ugly number.
//
// Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.
//
// Example:
//
//
// Input: n = 12, primes = [2,7,13,19]
// Output: 32 
// Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
//              super ugly numbers given primes = [2,7,13,19] of size 4.
//
// Note:
//
//
// 	1 is a super ugly number for any given primes.
// 	The given numbers in primes are in ascending order.
// 	0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
// 	The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
//
//


using pii = pair<int, int>;
class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        int k = primes.size();
        vector<int> res{1}, idx(k);
        priority_queue<pii, vector<pii>, greater<pii>> pq;
        int cnt = 0;
        for (const int p: primes){
            pq.push({p, cnt++});
        }
        while (res.size() < n){
            while ( !pq.empty() && pq.top().first <= res.back() ){

                int ind_prime = pq.top().second;
                pq.pop();
                idx[ind_prime]++;
                pq.push({primes[ind_prime] * res[idx[ind_prime]], ind_prime});
            }
            res.push_back(pq.top().first);
            pii top_ = pq.top();
            int ind_prime = top_.second;
            pq.pop();
            idx[ind_prime] ++;
            pq.push({primes[ind_prime] * res[idx[ind_prime]], ind_prime});
        }
        return res.back();
    }
};
