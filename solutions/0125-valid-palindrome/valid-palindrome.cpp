// Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
//
// Note: For the purpose of this problem, we define empty string as valid palindrome.
//
// Example 1:
//
//
// Input: "A man, a plan, a canal: Panama"
// Output: true
//
//
// Example 2:
//
//
// Input: "race a car"
// Output: false
//
//
//  
// Constraints:
//
//
// 	s consists only of printable ASCII characters.
//
//


class Solution {
public:
    bool isPalindrome(string s) {
        if (s.size() == 0) return true;
        string p = "";
        for (char c: s){
            char tmp = tolower(c);
            if (isalnum(tmp)){
                p += tmp;
            }
        }
        // cout << p << endl;
        if (p.size() == 0) return true;
        for (int i = 0; i <= p.size() / 2; i++){
            if (p[i] != p[p.size() - 1 - i]) return false;
        }
        return true; 
    }
};
