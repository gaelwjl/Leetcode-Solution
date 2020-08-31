// Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
//
//
// Note that it is the kth smallest element in the sorted order, not the kth distinct element.
//
//
// Example:
//
// matrix = [
//    [ 1,  5,  9],
//    [10, 11, 13],
//    [12, 13, 15]
// ],
// k = 8,
//
// return 13.
//
//
//
// Note: 
// You may assume k is always valid, 1 ≤ k ≤ n2.


class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        // use binary search
        int n = matrix.size();
        int lo = matrix[0][0], hi = matrix[n - 1][ n - 1];
        while (lo <= hi){
            
            int mid = lo + (hi - lo) / 2;
            int cnt = 0; // number of values <= than mid
            for (int i = 0; i < n; i++){
                vector<int> row = matrix[i];
                cnt += upper_bound(row.begin(), row.end(), mid) - row.begin();
            }
            // cout << mid << " " << cnt << endl;
            if (cnt >= k) hi = mid - 1;
            else lo = mid + 1;
        }
        return lo;
    }
};
