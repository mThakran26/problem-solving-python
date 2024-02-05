# LeetCode Interview 150: 3SUM
# Question Link: https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=top-interview-150

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if 
two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight 
without alerting the police.

"""


# Solution:

class Solution:
    def rob(self, nums: list[int]) -> int:
        prev = 0
        curr = 0
        for num in nums:
            temp = curr
            curr = max(num+prev, curr)
            prev = temp    
        return curr
