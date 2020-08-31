// Given two binary strings, return their sum (also a binary string).
//
// The input strings are both non-empty and contains only characters 1 or 0.
//
// Example 1:
//
//
// Input: a = "11", b = "1"
// Output: "100"
//
// Example 2:
//
//
// Input: a = "1010", b = "1011"
// Output: "10101"
//
//  
// Constraints:
//
//
// 	Each string consists only of '0' or '1' characters.
// 	1 <= a.length, b.length <= 10^4
// 	Each string is either "0" or doesn't contain any leading zero.
//
//


class Solution {
public:
    string addBinary(string a, string b) {
        int i = a.size() - 1, j = b.size() - 1; 
        string ans = "";
        int res = 0; 
        while (i >= 0 || j >= 0){
            int left = 0, right = 0; 
            if (i >= 0) left = a[i--] - '0';
            if (j >= 0) right = b[j--] - '0';
            ans += to_string((left + right + res) % 2);
            res = (left + right + res) / 2;
            // cout << ans << endl;
        }
        if (res) ans += to_string(res);
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
