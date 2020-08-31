// A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.
//
// Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level  i.e.  time[i]*satisfaction[i]
//
// Return the maximum sum of Like-time coefficient that the chef can obtain after dishes preparation.
//
// Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.
//
//  
// Example 1:
//
//
// Input: satisfaction = [-1,-8,0,5,-9]
// Output: 14
// Explanation: After Removing the second and last dish, the maximum total Like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14). Each dish is prepared in one unit of time.
//
// Example 2:
//
//
// Input: satisfaction = [4,3,2]
// Output: 20
// Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
//
//
// Example 3:
//
//
// Input: satisfaction = [-1,-4,-5]
// Output: 0
// Explanation: People don't like the dishes. No dish is prepared.
//
//
// Example 4:
//
//
// Input: satisfaction = [-2,5,-1,0,3,-3]
// Output: 35
//
//
//  
// Constraints:
//
//
// 	n == satisfaction.length
// 	1 <= n <= 500
// 	-10^3 <= satisfaction[i] <= 10^3
//


class Solution {
public:
    int maxSatisfaction(vector<int>& satisfaction) {
        vector<int> satis = satisfaction;
        sort(satis.begin(), satis.end());
        int scores = 0;
        int i = satis.size() - 1;
        for (; i>=0; i--){
            if (satis[i] < 0){
                int cum = 0;
                for (int j = i + 1; j < satis.size(); j++){
                    cum += satis[j];
                    if (cum + satis[i] >= 0)
                        break;
                }
                if (cum + satis[i] < 0) break;
            }
        }
        for (int j = i + 1; j <= satis.size() - 1; j++){
            scores += satis[j] * (j - i);
        }
        return scores;
    }
};
