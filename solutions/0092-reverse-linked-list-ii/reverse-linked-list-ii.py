# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.
#
# Example:
#
#
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        begin = head
        ans = ListNode()
        ans.next = head
        it_ans = ans
        for _ in range(m - 1):
            begin = begin.next
            it_ans = it_ans.next
        it_ans.next = None
        i = begin
        j = begin.next
        for _ in range(n - m):
            k = j.next
            j.next = i
            i = j
            j = k
        it_ans.next = i
        begin.next = j
        return ans.next
