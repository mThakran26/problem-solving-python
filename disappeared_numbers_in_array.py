#Question:  https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

#Solution: 
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        set_nums = set(nums)
        missing = []
        for i in range(1, len(nums)+1):
            if i not in set_nums:
                missing.append(i)
        return missing
