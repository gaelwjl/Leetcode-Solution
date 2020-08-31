# Sort a linked list in O(n log n) time using constant space complexity.
#
# Example 1:
#
#
# Input: 4->2->1->3
# Output: 1->2->3->4
#
#
# Example 2:
#
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(l1, l2):
            dummy = ListNode(0)
            cur = dummy
            while l1 and l2:
                if l1.val > l2.val: l1, l2 = l2, l1
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            if l1:
                cur.next = l1
            else:
                cur.next = l2
            return dummy.next
        if not head or not head.next: return head
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        return merge(self.sortList(head), self.sortList(mid))
