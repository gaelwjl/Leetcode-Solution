// Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
//
// Return list of lists of the suggested products after each character of searchWord is typed. 
//
//  
// Example 1:
//
//
// Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
// Output: [
// ["mobile","moneypot","monitor"],
// ["mobile","moneypot","monitor"],
// ["mouse","mousepad"],
// ["mouse","mousepad"],
// ["mouse","mousepad"]
// ]
// Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
// After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
// After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
//
//
// Example 2:
//
//
// Input: products = ["havana"], searchWord = "havana"
// Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
//
//
// Example 3:
//
//
// Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
// Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
//
//
// Example 4:
//
//
// Input: products = ["havana"], searchWord = "tatiana"
// Output: [[],[],[],[],[],[],[]]
//
//
//  
// Constraints:
//
//
// 	1 <= products.length <= 1000
// 	There are no repeated elements in products.
// 	1 <= Σ products[i].length <= 2 * 10^4
// 	All characters of products[i] are lower-case English letters.
// 	1 <= searchWord.length <= 1000
// 	All characters of searchWord are lower-case English letters.
//
//


class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        vector<vector<string>> ans;
        sort(products.begin(), products.end());
        string key;
        for (char c: searchWord){
            key += c;
            auto l = lower_bound(products.begin(), products.end(), key);
            auto r = upper_bound(products.begin(), products.end(), key + '~' );
            if (l == r)
                break;
            ans.emplace_back(l, min(l + 3, r));
        }
        while (ans.size() != searchWord.size())
            ans.push_back({});
        return ans;
        
    }
};
