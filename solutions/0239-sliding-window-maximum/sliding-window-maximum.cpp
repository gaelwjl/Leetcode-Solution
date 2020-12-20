// You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
//
// Return the max sliding window.
//
//  
// Example 1:
//
//
// Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
// Output: [3,3,5,5,6,7]
// Explanation: 
// Window position                Max
// ---------------               -----
// [1  3  -1] -3  5  3  6  7       3
//  1 [3  -1  -3] 5  3  6  7       3
//  1  3 [-1  -3  5] 3  6  7       5
//  1  3  -1 [-3  5  3] 6  7       5
//  1  3  -1  -3 [5  3  6] 7       6
//  1  3  -1  -3  5 [3  6  7]      7
//
//
// Example 2:
//
//
// Input: nums = [1], k = 1
// Output: [1]
//
//
// Example 3:
//
//
// Input: nums = [1,-1], k = 1
// Output: [1,-1]
//
//
// Example 4:
//
//
// Input: nums = [9,11], k = 2
// Output: [11]
//
//
// Example 5:
//
//
// Input: nums = [4,-2], k = 2
// Output: [4]
//
//
//  
// Constraints:
//
//
// 	1 <= nums.length <= 105
// 	-104 <= nums[i] <= 104
// 	1 <= k <= nums.length
//
//


#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
const ll inf = 2e9 + 7;
class Solution {
public:
    template<class T>
    struct RMQ {
        vector<vector<T>> jmp;

        RMQ(const vector<T> &V) : jmp(1, V) {
            for (int pw = 1, k = 1; pw * 2 <= sz(V); pw *= 2, ++k) {
                jmp.emplace_back(sz(V) - pw * 2 + 1);
                rep(j, 0, sz(jmp[k])) jmp[k][j] = max(jmp[k - 1][j], jmp[k - 1][j + pw]);
            }
        }

        T query(int a, int b) {
            assert(a < b); // or return inf if a == b 
            int dep = 31 - __builtin_clz(b - a);
            return max(jmp[dep][a], jmp[dep][b - (1 << dep)]);
        }
    };
    
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        RMQ<int> rmq(nums);
        vector<int> ans; 
        for (int i = 0; i + k - 1 < nums.size(); i++){
            ans.push_back(rmq.query(i, i + k)); 
        }
        return ans; 
    }
};
