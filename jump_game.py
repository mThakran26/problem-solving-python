# LeetCode Interview 150: JUMP GAME
# Question Link: https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150

"""

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your 
maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

"""


# Solution:
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        energy = 0
        for jump in nums:
            if energy < 0:
                return False
            if jump > energy:
                energy = jump
            energy-=1
        return True 