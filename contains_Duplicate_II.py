# LeetCode Interview 150: https://leetcode.com/problems/contains-duplicate-ii/description/?envType=study-plan-v2&envId=top-interview-150

# Question :

"""Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such
that nums[i] == nums[j] and abs(i - j) <= k."""

# Solution:
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        result = False
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                    if abs(i-j) <=k :
                        if nums[i] == nums[j]:
                            result = True
                            break
            
        return result