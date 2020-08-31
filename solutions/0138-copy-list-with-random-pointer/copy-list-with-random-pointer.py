# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.
#
# The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
#
#
# 	val: an integer representing Node.val
# 	random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
#
#
#  
# Example 1:
#
#
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
#
#
# Example 2:
#
#
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
#
#
# Example 3:
#
#
#
#
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
#
#
# Example 4:
#
#
# Input: head = []
# Output: []
# Explanation: Given linked list is empty (null pointer), so return null.
#
#
#  
# Constraints:
#
#
# 	-10000 <= Node.val <= 10000
# 	Node.random is null or pointing to a node in the linked list.
# 	Number of Nodes will not exceed 1000.
#
#


"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        clone_head = Node(head.val, None, None)
        
        curr = head
        curr_clone = clone_head
        
        seen = {}
        seen[head] = clone_head
        
        while curr:
            if curr.next:
                if curr.next not in seen:
                    curr_clone.next = Node(curr.next.val, None, None)
                    seen[curr.next] = curr_clone.next
                else:
                    curr_clone.next = seen[curr.next]
                
            if curr.random:
                if curr.random not in seen:
                    curr_clone.random = Node(curr.random.val, None, None)
                    seen[curr.random] = curr_clone.random
                else: 
                    curr_clone.random = seen[curr.random]
            
            curr = curr.next
            curr_clone = curr_clone.next
            seen[curr] = curr_clone
        return clone_head
