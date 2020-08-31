# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
#
#
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
#
# 	Only constant extra memory is allowed.
# 	You may not alter the values in the list's nodes, only nodes itself may be changed.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        it = head
        l = 0
        while it:
            it = it.next
            l += 1
            if l >= k:
                break
        if l < k:
            return head
        cur = head
        it = cur.next
        prev = None
        cnt = 1
        while cnt < k:
            cur.next = prev
            prev = cur
            cur = it
            if not it:
                return head
            it = it.next
            cnt += 1
        cur.next = prev
        head.next = self.reverseKGroup(it, k)
        return cur
            
