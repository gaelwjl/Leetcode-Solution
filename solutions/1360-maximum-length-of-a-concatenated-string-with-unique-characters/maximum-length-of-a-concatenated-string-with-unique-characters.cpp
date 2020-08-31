// Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.
//
// Return the maximum possible length of s.
//
//  
// Example 1:
//
//
// Input: arr = ["un","iq","ue"]
// Output: 4
// Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
// Maximum length is 4.
//
//
// Example 2:
//
//
// Input: arr = ["cha","r","act","ers"]
// Output: 6
// Explanation: Possible solutions are "chaers" and "acters".
//
//
// Example 3:
//
//
// Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
// Output: 26
//
//
//  
// Constraints:
//
//
// 	1 <= arr.length <= 16
// 	1 <= arr[i].length <= 26
// 	arr[i] contains only lower case English letters.
//
//


class Solution {
public:
    int maxLength(vector<string>& arr) {
        int n = arr.size();
        int ans = 0; 
        for (int i = 1; i < (1 << n); i++){
            vector<int> mask(26);
            int j = i; 
            int cnt = 0, tmp_l = 0;
            bool flag = false;
            while (j){
                if (j & 1){
                    for (char c: arr[cnt]){
                        if (mask[c - 'a']) {
                            flag = true;
                            break;
                        }
                        mask[c - 'a'] = 1;
                    }
                    tmp_l += arr[cnt].size();
                }
                j >>= 1; 
                cnt += 1;
            }
            if (!flag){
                ans = max(ans, tmp_l);
            }
        }
        return ans;
    }
};
