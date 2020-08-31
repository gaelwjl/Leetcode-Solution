# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
# Example 1:
#
#
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
#              because they are adjacent houses.
#
#
# Example 2:
#
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
#


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        def beginby(l):
            dp_y = [0 for _ in range(n)]
            dp_n = [0 for _ in range(n)]
            cnt = 0
            while cnt < n + 1:
                i = cnt % n
                if i != l:
                    dp_y[i] = dp_n[i - 1] + nums[i]
                    dp_n[i] = max(dp_y[i - 1], dp_n[i - 1])
                cnt += 1
            return max(max(dp_y), max(dp_n))
        ans1 = beginby(0)
        ans2 = beginby(1)
        return max(ans1, ans2)
