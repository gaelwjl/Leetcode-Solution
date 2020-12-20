// You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
//
// A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
//
// Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
//
//  
// Example 1:
//
//
//
//
// Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
// Output: 2
// Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
// This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
//
//
// Example 2:
//
//
//
//
// Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
// Output: 1
// Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
//
//
// Example 3:
//
//
// Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
// Output: 0
// Explanation: This route does not require any effort.
//
//
//  
// Constraints:
//
//
// 	rows == heights.length
// 	columns == heights[i].length
// 	1 <= rows, columns <= 100
// 	1 <= heights[i][j] <= 106
//
//


using node = pair<int, vector<int>> ;
class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int n = heights.size(), m = heights[0].size();
        vector<vector<int>> dist(n, vector<int>(m, INT_MAX));
        priority_queue<node, vector<node>, greater<>> pq;
        vector<int> dirs = {-1, 0, 1, 0, -1};
        vector<int> beg = {n - 1, m - 1};
        node init = make_pair(0, beg);
        pq.push(init);
        
        while (pq.size()){
            auto cur = pq.top();
            pq.pop();
            int x = cur.second[0], y = cur.second[1];
            if (x == 0 && y == 0){
                return cur.first;
            }
            for (int d = 0; d < 4; d++){
                int nx = x + dirs[d], ny = y + dirs[d+1];
                if ( nx >= 0 && ny >= 0 && nx < n && ny < m){
                    int tmp = max(abs(heights[x][y] - heights[nx][ny]), cur.first);
                    if (dist[nx][ny] > tmp){
                        dist[nx][ny] = tmp;
                        beg = {nx, ny};
                        pq.push(make_pair(tmp, beg));
                    }
                }
            }
        }
        return -1; 
    }
};
