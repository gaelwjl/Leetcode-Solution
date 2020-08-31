// Remove all elements from a linked list of integers that have value val.
//
// Example:
//
//
// Input:  1->2->6->3->4->5->6, val = 6
// Output: 1->2->3->4->5
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
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        
        ListNode* ans = new ListNode();
        ListNode* prev = ans;
        ListNode* it = head; 
        while (it != nullptr){
            if (it -> val != val){
                prev -> next = new ListNode(it -> val);
                prev = prev -> next; 
            }
            it = it -> next; 
        }
        return ans -> next;
    }
};
