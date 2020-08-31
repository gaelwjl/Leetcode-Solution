# Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
#
# After doing so, return the head of the final linked list.  You may return any such answer.
#
#  
# (Note that in the examples below, all sequences are serializations of ListNode objects.)
#
# Example 1:
#
#
# Input: head = [1,2,-3,3,1]
# Output: [3,1]
# Note: The answer [1,2,1] would also be accepted.
#
#
# Example 2:
#
#
# Input: head = [1,2,3,-3,4]
# Output: [1,2,4]
#
#
# Example 3:
#
#
# Input: head = [1,2,3,-3,-2]
# Output: [1]
#
#
#  
# Constraints:
#
#
# 	The given linked list will contain between 1 and 1000 nodes.
# 	Each node in the linked list has -1000 <= node.val <= 1000.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
      def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy.next    
        s = 0
        m = {s: dummy}
        while curr:
            s += curr.val
            #we should recompute the m
            if s in m:
                copy_b = m[s].next
                cum_b = s + copy_b.val
                while copy_b != curr:
                    del m[cum_b]
                    copy_b = copy_b.next
                    cum_b += copy_b.val
                m[s].next = curr.next
            else:
                m[s] = curr
            curr = curr.next
        return dummy.next
  #  [1,3,2,-3,-2,5,5,-5,1]
