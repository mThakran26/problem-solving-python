# LeetCode Interview 150: Rotate Array
# Question Link : https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
"""Given an integer array nums, rotate the array to the right by k steps, where k is non-negative."""


# Solution 1 (Brute Force): Time Exceeded in one test case 
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for _ in range(k):
            shift = nums[n-1]
            for i in range(n-1, -1, -1):
                nums[i] = nums[i-1]
            nums[0] = shift



# Solution 2: 
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % (len(nums))
        shift = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = shift