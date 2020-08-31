# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
#  
#
# Example:
#
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        i = head
        j = head
        if head:
            j = head.next
        else:
            return head
        while j:
            temp = j.next
            j.next = i
            i.next = temp
            pre.next = j
            if i.next and i.next.next:
                i = j.next.next
                j = i.next
                pre = pre.next.next
            else:
                break
        return dummy.next
