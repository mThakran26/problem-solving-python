# LeetCode - Interview 150
# Question link : https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150

# Solution:
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        for num in set(nums):
            count = nums.count(num)
            if count > (n/2):
                return num
                break