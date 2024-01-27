
# LeetCode 75: Remove Duplicates
# Question Link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Solution:a
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        i=0
        for j in range(1, n):
            if nums[i] != nums[j]:
                i+=1
                nums[i] = nums[j]

        return i+1






