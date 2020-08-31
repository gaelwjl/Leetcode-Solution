// Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
//
// Note that after backspacing an empty text, the text will continue empty.
//
//
// Example 1:
//
//
// Input: S = "ab#c", T = "ad#c"
// Output: true
// Explanation: Both S and T become "ac".
//
//
//
// Example 2:
//
//
// Input: S = "ab##", T = "c#d#"
// Output: true
// Explanation: Both S and T become "".
//
//
//
// Example 3:
//
//
// Input: S = "a##c", T = "#a#c"
// Output: true
// Explanation: Both S and T become "c".
//
//
//
// Example 4:
//
//
// Input: S = "a#c", T = "b"
// Output: false
// Explanation: S becomes "c" while T becomes "b".
//
//
// Note:
//
//
// 	1 <= S.length <= 200
// 	1 <= T.length <= 200
// 	S and T only contain lowercase letters and '#' characters.
//
//
// Follow up:
//
//
// 	Can you solve it in O(N) time and O(1) space?
//
//
//
//
//
//


class Solution {
public:
    stack<char> construct(string S){
        stack<char> s;
        for (char& c: S){
            if (c == '#' and s.size())
                s.pop();
            else if (c != '#')
                s.push(c);
        }
        return s;
    }
    bool backspaceCompare(string S, string T) {
        stack<char> s = construct(S), t = construct(T);
        if (s.size() != t.size())
            return false;
        while (s.size()){
            if (s.top() != t.top())
                return false;
            s.pop(), t.pop();
        }
        return true;
    }
};
