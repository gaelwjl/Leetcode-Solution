# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# Example:
#
#
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        smaller = ListNode(0)
        bigger = ListNode(0)
        itsmall = smaller
        itbigger = bigger
        it = head
        while (it != None):
            while it and it.val < x:
                itsmall.next = it
                itsmall = itsmall.next
                it = it.next
            itsmall.next = None
            while it and it.val >= x:
                itbigger.next = it
                itbigger = itbigger.next
                it = it.next
            itbigger.next = None
        itsmall.next = bigger.next
        return smaller.next
