# Question: https://leetcode.com/problems/binary-search/description/?envType=study-plan-v2&envId=binary-search

# Solution:
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1