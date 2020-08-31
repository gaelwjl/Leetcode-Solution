// Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
//
//
// For example:
// Given binary tree [3,9,20,null,null,15,7],
//
//     3
//    / \
//   9  20
//     /  \
//    15   7
//
//
//
// return its level order traversal as:
//
// [
//   [3],
//   [9,20],
//   [15,7]
// ]
//
//


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == nullptr){
            vector<vector<int>> tmp;
            return tmp;
        }
        deque<TreeNode*> tovis;
        tovis.push_back(root);
        vector<vector<int>> ans;
        while (!tovis.empty()){
            int s = tovis.size();
            vector<int> level; 
            while ( s-- ){
                auto cur = tovis.front();
                tovis.pop_front();
                level.push_back(cur -> val);
                if (cur -> left) tovis.push_back(cur -> left);
                if (cur -> right) tovis.push_back(cur ->right);
            }
            ans.push_back(level);
        }
        return ans;
    }
};
