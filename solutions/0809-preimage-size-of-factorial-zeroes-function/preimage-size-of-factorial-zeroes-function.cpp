// Let f(x) be the number of zeroes at the end of x!. (Recall that x! = 1 * 2 * 3 * ... * x, and by convention, 0! = 1.)
//
// For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) = 2 because 11! = 39916800 has 2 zeroes at the end. Given K, find how many non-negative integers x have the property that f(x) = K.
//
//
// Example 1:
// Input: K = 0
// Output: 5
// Explanation: 0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.
//
// Example 2:
// Input: K = 5
// Output: 0
// Explanation: There is no x such that x! ends in K = 5 zeroes.
//
//
// Note:
//
//
// 	K will be an integer in the range [0, 10^9].
//
//


class Solution {
public:
    using ll = long long; 
    int preimageSizeFZF(int K) {
        ll lb = 0, rb = 1e17;
        while (lb < rb){
            ll mid = lb + (rb - lb) / 2;
            ll k = trailingzeros(mid);
            if (k < K){
                lb = mid + 1;
            }
            else if (k > K){
                rb = mid - 1;
            }
            else return 5;
        }
        return 0;
    }
    
    ll trailingzeros(ll n){
        return n <= 1? 0 : n / 5 + trailingzeros(n / 5);
    }
};
