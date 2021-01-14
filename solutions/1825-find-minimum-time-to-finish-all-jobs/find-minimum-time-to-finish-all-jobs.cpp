// You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.
//
// There are k workers that you can assign jobs to. Each job should be assigned to exactly one worker. The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.
//
// Return the minimum possible maximum working time of any assignment. 
//
//  
// Example 1:
//
//
// Input: jobs = [3,2,3], k = 3
// Output: 3
// Explanation: By assigning each person one job, the maximum time is 3.
//
//
// Example 2:
//
//
// Input: jobs = [1,2,4,7,8], k = 2
// Output: 11
// Explanation: Assign the jobs the following way:
// Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
// Worker 2: 4, 7 (working time = 4 + 7 = 11)
// The maximum working time is 11.
//
//  
// Constraints:
//
//
// 	1 <= k <= jobs.length <= 12
// 	1 <= jobs[i] <= 107
//
//


class Solution {
public:
    int minimumTimeRequired(vector<int>& jobs, int k) {
        int n = jobs.size(), ans = INT_MAX;
        vector<int> loads(k); 
        // loads[i] represents the work load of the worker i; 
        sort(jobs.rbegin(), jobs.rend());
        function<void(int)> dfs = [&](int cur){
            if (cur == jobs.size()){
                ans = min(ans, *max_element(loads.begin(), loads.end()));
                return ; 
            }
            unordered_set<int> seen; 
            for (int i = 0; i < k; i++){
                // cut if already assign the same workload (symmetry) 
                if (seen.count(loads[i])) 
                    continue; 
                seen.insert(loads[i]); 
                loads[i] += jobs[cur];
                if (*max_element(loads.begin(), loads.end()) < ans)
                     dfs(cur + 1); 
                loads[i] -= jobs[cur]; 
            }
        };
        dfs(0); 
        return ans; 
    }
};
