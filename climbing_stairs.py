# LeetCode Interview 150: CLIMBING STAIRS
# Question Link: https://leetcode.com/problems/climbing-stairs/description/?envType=study-plan-v2&envId=top-interview-150

"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""

# Solution 1: This solution exceeds time limit


class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climbStairsRecursive(n, 0)
    
    def climbStairsRecursive(self, n: int , stair_sum: int) -> int:
        if n == stair_sum:
            return 1
        if n < stair_sum:
            return 0

        left_sum = self.climbStairsRecursive(n, stair_sum+1)
        right_sum = self.climbStairsRecursive(n, stair_sum+2)

        return left_sum+right_sum

# Solution 2: optimized
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]






