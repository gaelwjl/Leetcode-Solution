// Given a chemical formula (given as a string), return the count of each atom.
//
// An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
//
// 1 or more digits representing the count of that element may follow if the count is greater than 1.  If the count is 1, no digits will follow.  For example, H2O and H2O2 are possible, but H1O2 is impossible.
//
// Two formulas concatenated together produce another formula.  For example, H2O2He3Mg4 is also a formula.  
//
// A formula placed in parentheses, and a count (optionally added) is also a formula.  For example, (H2O2) and (H2O2)3 are formulas.
//
// Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.
//
// Example 1:
//
// Input: 
// formula = "H2O"
// Output: "H2O"
// Explanation: 
// The count of elements are {'H': 2, 'O': 1}.
//
//
//
// Example 2:
//
// Input: 
// formula = "Mg(OH)2"
// Output: "H2MgO2"
// Explanation: 
// The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
//
//
//
// Example 3:
//
// Input: 
// formula = "K4(ON(SO3)2)2"
// Output: "K4N2O14S4"
// Explanation: 
// The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
//
//
//
// Note:
// All atom names consist of lowercase letters, except for the first character which is uppercase.
// The length of formula will be in the range [1, 1000].
// formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.
//


class Solution {
    string s;
public:
    map<string, int> countOfAtoms(int& i){
        map<string, int> cnt;
        while (i < s.size()){
            if (s[i] == '('){
                const auto& tmp = countOfAtoms(++i);
                int mul = get_num(i);
                for (auto& kv: tmp){
                    cnt[kv.first] += mul * (kv.second);
                }
            }
            else if (s[i] == ')'){
                i++;
                return cnt;
            }
            else{
                string name = get_name(i);
                int mul = get_num(i);
                cnt[name] += mul;
            }
        }
        return cnt;
    }
    
    string countOfAtoms(string formula) {
        s = formula;
		int i = 0;
        map<string, int> cnt = countOfAtoms(i);
        string ans = "";
        for (auto& kv: cnt){
            ans += kv.first;
            if (kv.second > 1){
                ans += to_string(kv.second);
            }
        }
        return ans;
    }
    
    string get_name(int& i){
        string ans  = "";
        while (i < s.size() && (ans.size() == 0 || islower(s[i]))){
            ans += s[i++];
        }
        return ans;
    }
    
    int get_num(int& i){
        string ans = "";
        while (i < s.size() && isdigit(s[i])){
            ans += s[i++];
        }
        return ans.size() == 0 ? 1: stoi(ans);
    }

};
