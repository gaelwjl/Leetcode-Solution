# You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has the same maximum capacity.
#
# Implement the DinnerPlates class:
#
#
# 	DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks.
# 	void push(int val) pushes the given positive integer val into the leftmost stack with size less than capacity.
# 	int pop() returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns -1 if all stacks are empty.
# 	int popAtStack(int index) returns the value at the top of the stack with the given index and removes it from that stack, and returns -1 if the stack with that given index is empty.
#
#
# Example:
#
#
# Input: 
# ["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
# [[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
# Output: 
# [null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]
#
# Explanation: 
# DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
# D.push(1);
# D.push(2);
# D.push(3);
# D.push(4);
# D.push(5);         // The stacks are now:  2  4
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.popAtStack(0);   // Returns 2.  The stacks are now:     4
#                                                        1  3  5
#                                                        ﹈ ﹈ ﹈
# D.push(20);        // The stacks are now: 20  4
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.push(21);        // The stacks are now: 20  4 21
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
#                                                         1  3  5
#                                                         ﹈ ﹈ ﹈
# D.popAtStack(2);   // Returns 21.  The stacks are now:     4
#                                                         1  3  5
#                                                         ﹈ ﹈ ﹈ 
# D.pop()            // Returns 5.  The stacks are now:      4
#                                                         1  3 
#                                                         ﹈ ﹈  
# D.pop()            // Returns 4.  The stacks are now:   1  3 
#                                                         ﹈ ﹈   
# D.pop()            // Returns 3.  The stacks are now:   1 
#                                                         ﹈   
# D.pop()            // Returns 1.  There are no stacks.
# D.pop()            // Returns -1.  There are still no stacks.
#
#
#  
# Constraints:
#
#
# 	1 <= capacity <= 20000
# 	1 <= val <= 20000
# 	0 <= index <= 100000
# 	At most 200000 calls will be made to push, pop, and popAtStack.
#
#


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capa = capacity
        self.stacks = [[] for _ in range(101)]
        self.vacant = 0
        self.leftest = 0
        
    def push(self, val: int) -> None:
        if self.vacant == len(self.stacks) - 1:
            self.stacks.extend([[] for _ in range(101)])
        for i in range(self.vacant, len(self.stacks)):
            curr = self.stacks[i]
            if len(curr) < self.capa:
                curr.append(val)
                self.vacant = i
                self.leftest = max(self.leftest, i)
                break

            
    def pop(self) -> int:
        if self.leftest == 0 and len(self.stacks[self.leftest]) == 0:
            return -1
        if len(self.stacks[self.leftest]) == 0:
            self.leftest -= 1
            self.vacant = min(self.leftest, self.vacant)
            return self.pop()
        return self.stacks[self.leftest].pop(-1)

    def popAtStack(self, index: int) -> int:
        self.vacant = min(self.vacant, index)
        if len(self.stacks[index]) == 0:
            return -1
        else:
            return self.stacks[index].pop(-1)


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
