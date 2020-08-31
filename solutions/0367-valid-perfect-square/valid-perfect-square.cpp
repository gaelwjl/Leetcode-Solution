// Given a positive integer num, write a function which returns True if num is a perfect square else False.
//
// Follow up: Do not use any built-in library function such as sqrt.
//
//  
// Example 1:
// Input: num = 16
// Output: true
// Example 2:
// Input: num = 14
// Output: false
//
//  
// Constraints:
//
//
// 	1 <= num <= 2^31 - 1
//
//


class Solution {
public:
    bool isPerfectSquare(int num) {
        long long left = 0, right = num;
        while (left < right){
            long long mid = (left + right) / 2;
            if (mid * mid >= num)
                right = mid;
            else
                left = mid + 1;
        }
        if (left*left == num)
            return true;
        return false;
    }
};
