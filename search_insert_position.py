# Question: https://leetcode.com/problems/search-insert-position/description/?envType=study-plan-v2&envId=binary-search

# Solution:
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                return i
            elif target > nums[-1]:
                return n
            elif target < nums[0]:
                return 0
            elif i+1 < n:
                if nums[0] < target < nums[i+1]:
                    return i+1