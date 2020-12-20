// You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
//
// Merge all the linked-lists into one sorted linked-list and return it.
//
//  
// Example 1:
//
//
// Input: lists = [[1,4,5],[1,3,4],[2,6]]
// Output: [1,1,2,3,4,4,5,6]
// Explanation: The linked-lists are:
// [
//   1->4->5,
//   1->3->4,
//   2->6
// ]
// merging them into one sorted list:
// 1->1->2->3->4->4->5->6
//
//
// Example 2:
//
//
// Input: lists = []
// Output: []
//
//
// Example 3:
//
//
// Input: lists = [[]]
// Output: []
//
//
//  
// Constraints:
//
//
// 	k == lists.length
// 	0 <= k <= 10^4
// 	0 <= lists[i].length <= 500
// 	-10^4 <= lists[i][j] <= 10^4
// 	lists[i] is sorted in ascending order.
// 	The sum of lists[i].length won't exceed 10^4.
//
//


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
// write a cmp for listNode; 
class cmp{
    public:
    bool operator() (ListNode* left, ListNode* right)
    {
        return left -> val >= right -> val;
    }
};
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode* ans = new ListNode(0);
        auto it_ans = ans;
        int n = lists.size();
        priority_queue<ListNode*, vector<ListNode*>,  cmp> pq; 
        for (auto v: lists)
            if(v) pq.push(v);
        
        while (pq.size()){
            auto it = pq.top();
            pq.pop();
            if (it == nullptr) 
                continue;
            it_ans -> next = it;
            it_ans = it_ans -> next;
            if (it -> next)
                pq.push(it -> next);
            it_ans -> next = nullptr;
        }
        return ans -> next;
    }
};
