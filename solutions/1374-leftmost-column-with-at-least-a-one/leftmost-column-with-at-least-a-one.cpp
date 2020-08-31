// (This problem is an interactive problem.)
//
// A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.
//
// Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.
//
// You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:
//
//
// 	BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
// 	BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which means the matrix is rows * cols.
//
//
// Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.
//
// For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.
//
//  
//
//  
//
//  
// Example 1:
//
//
//
//
// Input: mat = [[0,0],[1,1]]
// Output: 0
//
//
// Example 2:
//
//
//
//
// Input: mat = [[0,0],[0,1]]
// Output: 1
//
//
// Example 3:
//
//
//
//
// Input: mat = [[0,0],[0,0]]
// Output: -1
//
// Example 4:
//
//
//
//
// Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
// Output: 1
//
//
//  
// Constraints:
//
//
// 	rows == mat.length
// 	cols == mat[i].length
// 	1 <= rows, cols <= 100
// 	mat[i][j] is either 0 or 1.
// 	mat[i] is sorted in a non-decreasing way.
//


/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * class BinaryMatrix {
 *   public:
 *     int get(int x, int y);
 *     vector<int> dimensions();
 * };
 */

class Solution {
public:
    int leftMostColumnWithOne(BinaryMatrix &binaryMatrix) {
        int n = binaryMatrix.dimensions()[0], m = binaryMatrix.dimensions()[1];
        int ls = 0, rs = m - 1;
        while (ls < rs){
            //cout << ls << " " << rs << endl;
            int mid = (ls + rs) / 2;
            int cum  = 0;
            for(int j = n - 1; j >= 0; j--){
                int cur = binaryMatrix.get(j, mid);
                cum += cur;
                if (cum >= 2) break;
            }
            if (cum >= 1)
                rs = mid;
            else
                ls = mid + 1;
        }
        //cout << ls << endl;
        int cum  = 0;
        {
            int j = n - 1;
            for(; j >= 0; j--){
                int cur = binaryMatrix.get(j, ls);
                cum += cur;
                if (cum >= 2) return ls;
            }
        }
        if (cum == 1)
            return ls;
        else
            return -1;
        
    }
};
