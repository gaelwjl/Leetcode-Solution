// Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A exactly K times so that the resulting string equals B.
//
// Given two anagrams A and B, return the smallest K for which A and B are K-similar.
//
// Example 1:
//
//
// Input: A = "ab", B = "ba"
// Output: 1
//
//
//
// Example 2:
//
//
// Input: A = "abc", B = "bca"
// Output: 2
//
//
//
// Example 3:
//
//
// Input: A = "abac", B = "baca"
// Output: 2
//
//
//
// Example 4:
//
//
// Input: A = "aabc", B = "abca"
// Output: 2
//
//
//
//
// Note:
//
//
// 	1 <= A.length == B.length <= 20
// 	A and B contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}
//
//


class Solution {
public:
    int kSimilarity(string A, string B) {
        deque<string> tosee{A}; 
        unordered_set<string> seen; 
        int k = 0;
        while (tosee.size()){
            int n = tosee.size(); while (n--){
                auto cur = tosee.front();
                tosee.pop_front();
                if (seen.count(cur)) 
                    continue;
                seen.insert(cur);
                // cout << cur << endl;
                if (cur == B)
                    return k;
                int beg = 0; 
                for (; cur[beg] == B[beg]; beg++);
                for (int i = beg; i < A.size(); i++){
                    if (cur[i] != B[beg])
                        continue;
                    swap(cur[i], cur[beg]);
                    if (!seen.count(cur)){
                        tosee.push_back(cur);
                    }
                    swap(cur[i], cur[beg]);
                }
                
            }
            k++;
        }
        return -1;
    }
};
