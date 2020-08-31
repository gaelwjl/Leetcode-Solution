# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        cur_res = res
        
        carry = 0
        while l1 != None or l2 != None:
            l1_v = 0
            l2_v = 0
            if l1 != None:
                l1_v  = l1.val
                l1 = l1.next
            if l2 != None:
                l2_v = l2.val
                l2 = l2.next
            temp = (carry + l1_v + l2_v)
            
            cur_res.next = ListNode(temp % 10)
            cur_res = cur_res.next
            
            carry = temp // 10
        
        while carry > 0:
            cur_res.next = ListNode(carry % 10)
            cur_res = cur_res.next
            carry = carry // 10
            
        return res.next
            
