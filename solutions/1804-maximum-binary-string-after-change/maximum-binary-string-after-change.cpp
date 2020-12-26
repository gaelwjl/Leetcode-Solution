// You are given a binary string binary consisting of only 0's or 1's. You can apply each of the following operations any number of times:
//
//
// 	Operation 1: If the number contains the substring "00", you can replace it with "10".
//
//
// 		For example, "00010" -> "10010"
//
//
// 	Operation 2: If the number contains the substring "10", you can replace it with "01".
//
// 		For example, "00010" -> "00001"
//
//
//
//
// Return the maximum binary string you can obtain after any number of operations. Binary string x is greater than binary string y if x's decimal representation is greater than y's decimal representation.
//
//  
// Example 1:
//
//
// Input: binary = "000110"
// Output: "111011"
// Explanation: A valid transformation sequence can be:
// "000110" -> "000101" 
// "000101" -> "100101" 
// "100101" -> "110101" 
// "110101" -> "110011" 
// "110011" -> "111011"
//
//
// Example 2:
//
//
// Input: binary = "01"
// Output: "01"
// Explanation: "01" cannot be transformed any further.
//
//
//  
// Constraints:
//
//
// 	1 <= binary.length <= 105
// 	binary consist of '0' and '1'.
//
//


class Solution {
public:
    string maximumBinaryString(string b) {
        int i = 0, j = b.size() - 1;
        for (; i < b.size() && b[i] == '1'; i++); 
        for (; j>=0 && b[j] == '1';j--); 
        if (j < i) return b; 
        return b.substr(0, i) + help(b.substr(i, j - i + 1)) + b.substr(j + 1, b.size() - j - 1);
        
    }
    string help(string b){
        int cnt = 0; 
        for (char c: b){
            cnt += c - '0'; 
        }
        string ans = ""; 
        int n = b.size(); 
        if (n - cnt > 0){
            for (int i = 0; i < n - cnt - 1; i++){
                ans += '1'; 
            }
            ans += '0';
        }
        for (int i = 0; i < cnt; i++){
            ans += '1'; 
        }
        return ans; 
    }
};
