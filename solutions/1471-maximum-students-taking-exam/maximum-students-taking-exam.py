# -*- coding:utf-8 -*-


# Given a m * n matrix seats  that represent seats distributions in a classroom. If a seat is broken, it is denoted by '#' character otherwise it is denoted by a '.' character.
#
# Students can see the answers of those sitting next to the left, right, upper left and upper right, but he cannot see the answers of the student sitting directly in front or behind him. Return the maximum number of students that can take the exam together without any cheating being possible..
#
# Students must be placed in seats in good condition.
#
#  
# Example 1:
#
#
# Input: seats = [["#",".","#","#",".","#"],
#                 [".","#","#","#","#","."],
#                 ["#",".","#","#",".","#"]]
# Output: 4
# Explanation: Teacher can place 4 students in available seats so they don't cheat on the exam. 
#
#
# Example 2:
#
#
# Input: seats = [[".","#"],
#                 ["#","#"],
#                 ["#","."],
#                 ["#","#"],
#                 [".","#"]]
# Output: 3
# Explanation: Place all students in available seats. 
#
#
#
# Example 3:
#
#
# Input: seats = [["#",".",".",".","#"],
#                 [".","#",".","#","."],
#                 [".",".","#",".","."],
#                 [".","#",".","#","."],
#                 ["#",".",".",".","#"]]
# Output: 10
# Explanation: Place students in available seats in column 1, 3 and 5.
#
#
#  
# Constraints:
#
#
# 	seats contains only characters '.' and'#'.
# 	m == seats.length
# 	n == seats[i].length
# 	1 <= m <= 8
# 	1 <= n <= 8
#
#


class Solution(object):
    def maxStudents(self, seats):
        """
        :type seats: List[List[str]]
        :rtype: int
        """
        m = len(seats)
        n = len(seats[0])
        dp = [[0] * (1 << n) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1 << n):
                for k in range(1 << n):
                    #determiner dp[i][k] knowing dp[i - 1][j]
                    #attention to parentheses 
                    flag = True
                    temp = 0
                    for k_iter in range(n):
                        if not ((1 << k_iter) & k):
                            continue
                        if seats[i - 1][k_iter] == '#' or (k_iter > 0 and ((1 << (k_iter - 1)) & k)) or (k_iter < n - 1 and ((1 << (k_iter + 1)) & k)):
                            flag = False
                            break
                        if (k_iter >= 1 and (1 << (k_iter - 1) & j)) or (k_iter < n - 1 and (1 << (k_iter + 1) & j)):
                            flag = False
                            break
                        temp += 1
                    if flag: 
                        dp[i][k] = max(dp[i][k], dp[i - 1][j] + temp)
        return max(dp[m])
