// In an N by N square grid, each cell is either empty (0) or blocked (1).
//
// A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:
//
//
// 	Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
// 	C_1 is at location (0, 0) (ie. has value grid[0][0])
// 	C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
// 	If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
//
//
// Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.
//
//  
//
// Example 1:
//
//
// Input: [[0,1],[1,0]]
//
//
// Output: 2
//
//
//
//
// Example 2:
//
//
// Input: [[0,0,0],[1,1,0],[1,1,0]]
//
//
// Output: 4
//
//
//
//  
//
//
// Note:
//
//
// 	1 <= grid.length == grid[0].length <= 100
// 	grid[r][c] is 0 or 1
//
//


using pii = pair<int, int>;
class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        deque<pii> q;
        q.push_back({0, 0});
        int steps = 1;
        int n = grid.size();
        while (!q.empty()){
            int s = q.size();
            while (s--){
            pii cur = q.front();
            q.pop_front();
            int x = cur.first, y = cur.second;
            if (grid[x][y] == 1) continue;
            // cout << x << " " << y << endl;
            grid[x][y] = 1;
            if (x == n - 1 && y == n - 1) return steps;
            for (int nx = max(x - 1, 0); nx <= min(x + 1, n - 1); nx ++){
                for (int ny = max(y - 1, 0); ny <= min(y + 1, n - 1); ny ++){
                    // cout << nx << " " << ny << endl;
                    if ((nx != x || ny != y) && grid[nx][ny] != 1)
                        q.push_back({nx, ny});
                    }
                }
            }
            steps += 1;
        }
        return -1;
    }
};

