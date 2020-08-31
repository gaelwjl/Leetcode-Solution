# Given an array of linked-lists lists, each linked list is sorted in ascending order.
#
# Merge all the linked-lists into one sort linked-list and return it.
#
#  
# Example 1:
#
#
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
#
#
# Example 2:
#
#
# Input: lists = []
# Output: []
#
#
# Example 3:
#
#
# Input: lists = [[]]
# Output: []
#
#
#  
# Constraints:
#
#
# 	k == lists.length
# 	0 <= k <= 10^4
# 	0 <= lists[i].length <= 500
# 	-10^4 <= lists[i][j] <= 10^4
# 	lists[i] is sorted in ascending order.
# 	The sum of lists[i].length won't exceed 10^4.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #to change not to use extra memory:
        if len(lists) == 0:
            return None
        def merge2Lists(l1, l2):
            res = ListNode(0)
            cur = res
            while l1 and l2:
                if l1.val > l2.val: l1, l2 = l2, l1
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            cur.next = l1 if l1 else l2
            return res.next
        #note that there is a big difference if we don't use
        #divide and conquer
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists
